from urllib.parse import urlparse
import argparse
import ast
#import ftplib
import logging
import multiprocessing
import os
import paramiko
import requests
import requests_ftp
import socket
import sys
import time


FILE, LOG_PATH = 'file', 'logs'


class Protocol:
    HTTP, HTTPS, FTP, SFTP = 'http', 'https', 'ftp', 'sftp'


class Item:
    URL, PORT, REMOTE_PATH, FILENAME, LOCAL_PATH, USER, PASSWORD = 'url', 'port', 'remote', 'filename', 'local', 'user', 'password'


def mkdirIfNotExist(path):
    try:
        os.listdir(path)
    except FileNotFoundError:
        os.mkdir(path)


def getFilename(filename):
    if filename is None:
        return None
    try:
        slashIdx = filename.rindex(os.path.sep)
        if -1 < slashIdx:
            return filename[slashIdx + 1:]
    except ValueError:
        pass
    return filename


class Downloader:
    @classmethod
    def factory(cls, item):
        def getKeyValue(key):
            return item[key] if key in item else None

        url = getKeyValue(Item.URL)
        port = getKeyValue(Item.PORT)
        remote = getKeyValue(Item.REMOTE_PATH)
        filename = getKeyValue(Item.FILENAME)
        local = getKeyValue(Item.LOCAL_PATH)
        user = getKeyValue(Item.USER)
        password = getKeyValue(Item.PASSWORD)

        if url is None or 0 == len(url):
            return None

        #   urlparse returns at lease 0-length string even if input url is None
        #   So, do NOT need to check exception
        scheme = urlparse(url).scheme

        if scheme in [Protocol.HTTP, Protocol.HTTPS]:
            return HttpDownloader(url, local)
        elif Protocol.FTP == scheme:
            return FtpDownloader(url, port, remote, filename, local, user, password)
        elif Protocol.SFTP == scheme:
            return SftpDownloader(url, port, remote, filename, local, user, password)
        return None

    def __init__(self, url, port, remote, filename, local, user, password):
        self.url = url
        self.port = port
        self.remote = remote
        self.filename = getFilename(filename)
        self.local = local
        if self.local:
            mkdirIfNotExist(self.local)
        else:
            self.local = '.'
        self.user = user
        self.password = password

        self.parsedUrl = urlparse(self.url)
        if self.filename is None:
            self.filename = getFilename(self.parsedUrl.path)
        self.localFilepath = os.path.join(self.local, self.filename)
        self.downloadingLocalFilepath = '{}.{}_downloading'.format(self.localFilepath, self.parsedUrl.scheme)
        self.logger = self.get_logger()

    def download(self):
        pass

    def get_logger(self):
        name = multiprocessing.current_process().name
        h = logging.FileHandler('{}/{}.log'.format(LOG_PATH, name))
        FORMAT = "%(asctime)s [%(levelname)s][%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
        h.setFormatter(logging.Formatter(FORMAT))
        logger = logging.getLogger(name)
        logger.addHandler(h)
        logger.setLevel(logging.DEBUG)
        return logger


#   https://gist.github.com/hyunjun/11f8c7ee9d5a5c4dd2804071dd4f5ab2#file-file_download-md
class HttpDownloader(Downloader):
    def __init__(self, url, local='.'):
        super(self.__class__, self).__init__(url, None, None, None, local, None, None)

        self.CHUNK_SIZE = 512   #   TODO: very small number on purpose
        self.TIMEOUT = 1   #   TODO: what is proper timeout?

    def getFilesize(self):
        size = 0
        try:
            with open(self.downloadingLocalFilepath, 'r') as f:
                f.seek(0, os.SEEK_END)
                size = f.tell()
        except FileNotFoundError:
            pass
        return size

    def getRemoteFilesize(self):
        try:
            return int(requests.get(self.url, stream=True).headers['Content-length'])
        except:
            pass
        return None

    def download(self):
        startTime = time.time()

        resumeHeader, filesize, remoteFilesize = None, self.getFilesize(), self.getRemoteFilesize()
        if remoteFilesize is None:
            self.logger.error('Exception happened while get the remote file size of {}'.format(self.filename))
            return

        if 0 < filesize < remoteFilesize:
            resumeHeader = {'Range': 'bytes={}-'.format(filesize)}
        elif 0 != filesize:
            self.logger.error('Did you already download {}? A local file size is {}, while the remote one {}'.format(self.filename, filesize, remoteFilesize))
            return

        resp, mode = None, None
        try:
            if resumeHeader:
                self.logger.debug('Resume downloading {} from size {}'.format(self.filename, filesize))
                resp, mode = requests.get(self.url, headers=resumeHeader, stream=True, timeout=self.TIMEOUT), 'ab'
            else:
                self.logger.debug('Start downloading {} from size 0'.format(self.filename))
                resp, mode = requests.get(self.url, stream=True, timeout=self.TIMEOUT), 'wb'
        except requests.exceptions.Timeout:
            self.logger.error('Timeout happened while downloading {}'.format(self.filename))
        except requests.exceptions.ConnectionError:
            self.logger.error('ConnectionError happened while downloading {}'.format(self.filename))

        if resp:
            if requests.codes.ok == resp.status_code:
                with open(self.downloadingLocalFilepath, mode) as f:
                    for chunk in resp.iter_content(chunk_size=self.CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
                os.rename(self.downloadingLocalFilepath, self.localFilepath)

                elapsedTime = time.time() - startTime
                self.logger.debug('Downloading {} completed'.format(self.filename))
                self.logger.debug('Elapsed time {0:.2f} sec'.format(elapsedTime))
            else:
                self.logger.error('Something wrong while downloading {}. Status code is {}'.format(self.filename, resp.status_code))


#   https://gist.github.com/hyunjun/11f8c7ee9d5a5c4dd2804071dd4f5ab2#file-ftp-md
class FtpDownloader(Downloader):
    def __init__(self, url, port=21, remote=None, filename=None, local='.', user='anonymous', password='anonymous'):
        super(self.__class__, self).__init__(url, port, remote, filename, local, user, password)

        if self.port is None:
            self.port = 21
        if self.user is None:
            self.user = 'anonymous'
        if self.password is None:
            self.password = 'anonymous'

        #self.ftp = ftplib.FTP()
        requests_ftp.monkeypatch_session()
        self.s = requests.Session()

    #def connect(self):
    #    print(self.parsedUrl.netloc, self.port)
    #    self.ftp.connect(self.parsedUrl.netloc, self.port)
    #    try:
    #        self.ftp.login(self.user, self.password)
    #    except EOFError:
    #        pass
    #    if self.remote:
    #        self.ftp.cwd(self.remote)
    #    self.ftp.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    #    self.ftp.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 75)
    #    #self.ftp.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)

    def download(self):
        startTime = time.time()

        #self.ftp.set_debuglevel(2)
        #self.ftp.set_pasv(True)
        #self.connect()
        #self.ftp.voidcmd('Type I')

        #filesize = self.ftp.size(self.filename)
        #with open(self.filename, 'w+b') as f:
        #    while f.tell() < filesize:
        #        try:
        #            self.connect()
        #            res = ftp.retrbinary('RETR {}'.format(self.filename), f.write) if f.tell() == 0 else ftp.retrbinary('RETR {}'.format(self.filename), f.write, rest=f.tell())
        #        except:
        #            self.logger.debug('Reconnect to ftp')
        #self.ftp.quit()

        if self.remote:
            ftpAddr = '{}:{}/{}/{}'.format(self.url, self.port, self.remote, self.filename)
        else:
            ftpAddr = '{}:{}/{}'.format(self.url, self.port, self.filename)

        resp = None
        try:
            resp = self.s.get(ftpAddr, auth=(self.user, self.password))
        except requests.exceptions.ConnectionError:
            self.logger.error('ConnectionError happened while downloading {}'.format(self.filename))

        if resp:
            if requests.codes.ok == resp.status_code:
                with open(self.downloadingLocalFilepath, 'wb') as f:
                    f.write(resp.content)
                os.rename(self.downloadingLocalFilepath, self.localFilepath)

                elapsedTime = time.time() - startTime
                self.logger.debug('Downloading {} completed'.format(self.filename))
                self.logger.debug('Elapsed time {0:.2f} sec'.format(elapsedTime))
            else:
                self.logger.error('Something wrong while downloading {}. Status code is {}'.format(self.filename, resp.status_code))


#   https://gist.github.com/hyunjun/11f8c7ee9d5a5c4dd2804071dd4f5ab2#file-sftp-md
class SftpDownloader(Downloader):
    def __init__(self, url, port=22, remote=None, filename=None, local='.', user='anonymous', password='anonymous'):
        super(self.__class__, self).__init__(url, port, remote, filename, local, user, password)

        if self.port is None:
            self.port = 22
        if self.user is None:
            self.user = 'anonymous'
        if self.password is None:
            self.password = 'anonymous'

        self.client = paramiko.SSHClient()

    def download(self):
        class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
            def missing_host_key(self, client, hostname, key):
                return

        startTime = time.time()

        self.client.set_missing_host_key_policy(AllowAnythingPolicy())
        sftp = None
        try:
            self.client.connect(self.parsedUrl.netloc, port=self.port, username=self.user, password=self.password)
            sftp = self.client.open_sftp()
        except TimeoutError:
            self.logger.error('TimeoutError happened while downloading {}'.format(self.filename))
        except paramiko.ssh_exception.BadHostKeyException:
            self.logger.error('BadHostKeyException happened while downloading {}'.format(self.filename))
        except paramiko.ssh_exception.AuthenticationException:
            self.logger.error('AuthenticationException happened while downloading {}'.format(self.filename))
        except paramiko.ssh_exception.SSHException:
            self.logger.error('SSHException happened while downloading {}'.format(self.filename))
        except socket.error:
            self.logger.error('Socket error happened while downloading {}'.format(self.filename))

        if sftp:
            if self.remote:
                sftp.chdir(self.remote)
            sftp.get(self.filename, self.downloadingLocalFilepath)
            os.rename(self.downloadingLocalFilepath, self.localFilepath)
            self.client.close()

            elapsedTime = time.time() - startTime
            self.logger.debug('Downloading {} completed'.format(self.filename))
            self.logger.debug('Elapsed time {0:.2f} sec'.format(elapsedTime))


def download(item):
    downloader = Downloader.factory(item)
    if downloader:
        downloader.download()


def options(argv):
    parser = argparse.ArgumentParser(description='Downloader')
    parser.set_defaults(command=None)

    subparsers = parser.add_subparsers(help='sub commands')

    http_parser = subparsers.add_parser(Protocol.HTTP, help='Download file from http(s) url')
    http_parser.add_argument(Item.URL, action='store', help='Url to download file')
    http_parser.add_argument('--local-path', action='store', dest=Item.LOCAL_PATH, default='.')
    http_parser.set_defaults(command=Protocol.HTTP)

    ftp_parser = subparsers.add_parser(Protocol.FTP, help='Download file from (s)ftp address')
    ftp_parser.add_argument(Item.URL, action='store', help='Ftp address to download file')
    ftp_parser.add_argument('--port', action='store', dest=Item.PORT, default=21)
    ftp_parser.add_argument('--remote-path', action='store', dest=Item.REMOTE_PATH, default=None)
    ftp_parser.add_argument('--filename', action='store', dest=Item.FILENAME, default=None)
    ftp_parser.add_argument('--local-path', action='store', dest=Item.LOCAL_PATH, default='.')
    ftp_parser.add_argument('--user', action='store', dest=Item.USER, default='anonymous')
    ftp_parser.add_argument('--password', action='store', dest=Item.PASSWORD, default='anonymous')
    ftp_parser.set_defaults(command=Protocol.FTP)

    file_parser = subparsers.add_parser(FILE, help='Download file from configuration file')
    file_parser.add_argument(Item.FILENAME, action='store', help='Configuration file name')
    file_parser.set_defaults(command=FILE)

    option = parser.parse_args(argv[1:])
    return option


if __name__ == '__main__':
    option, items = options(sys.argv), []
    if option.command is None:
        print("Execute with '--help' to see how to use")
        sys.exit(1)

    #   create log directory if it does NOT exist
    mkdirIfNotExist(LOG_PATH)

    print(option)
    if Protocol.HTTP == option.command:
        items.append({Item.URL: option.url, Item.LOCAL_PATH: option.local})

    elif Protocol.FTP == option.command:
        items.append({Item.URL: option.url, Item.PORT: option.port, Item.REMOTE_PATH: option.remote, Item.FILENAME: option.filename, Item.LOCAL_PATH: option.local, Item.USER: option.user, Item.PASSWORD: option.password})

    elif FILE == option.command:
        with open(option.filename, 'r') as f:
            for line in f.readlines():
                try:
                    d = ast.literal_eval(line.strip())
                    items.append(d)
                except SyntaxError:
                    print('Cannot process {}'.format(line.strip()))

    #   Download files using multiprocessing
    jobs = []
    for item in items:
        print(item)
        job = multiprocessing.Process(target=download, args=(item,))
        jobs.append(job)
        job.start()

    for job in jobs:
        job.join()
