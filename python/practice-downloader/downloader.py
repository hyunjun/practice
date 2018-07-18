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
    URL, PORT, PATH, FILENAME, USER, PASSWORD = 'url', 'port', 'path', 'filename', 'user', 'password'


class Downloader:
    @classmethod
    def factory(cls, item):
        def getKeyValue(key):
            return item[key] if key in item else None

        url = getKeyValue(Item.URL)
        port = getKeyValue(Item.PORT)
        path = getKeyValue(Item.PATH)
        filename = getKeyValue(Item.FILENAME)
        user = getKeyValue(Item.USER)
        password = getKeyValue(Item.PASSWORD)

        if url is None or 0 == len(url):
            return None

        #   urlparse returns at lease 0-length string even if input url is None
        #   So, do NOT need to check exception
        scheme = urlparse(url).scheme

        if scheme in [Protocol.HTTP, Protocol.HTTPS]:
            return HttpDownloader(url)
        elif Protocol.FTP == scheme:
            return FtpDownloader(url, port, path, filename, user, password)
        elif Protocol.SFTP == scheme:
            return SftpDownloader(url, port, path, filename, user, password)
        return None

    def __init__(self, url, port, path, filename, user, password):
        self.url = url
        self.port = port
        self.path = path
        self.filename = filename
        self.user = user
        self.password = password

        self.parsedUrl = urlparse(self.url)
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
    def __init__(self, url):
        super(self.__class__, self).__init__(url, None, None, None, None, None)

        self.filename = self.getFilename()
        self.CHUNK_SIZE = 512   #   TODO: very small number on purpose

    def getFilename(self):
        slashIdx = self.parsedUrl.path.rindex(os.path.sep)
        if -1 < slashIdx:
            return self.parsedUrl.path[slashIdx + 1:]
        return None

    def getFilesize(self):
        size = 0
        try:
            with open(self.filename, 'r') as f:
                f.seek(0, os.SEEK_END)
                size = f.tell()
        except FileNotFoundError:
            pass
        return size

    def download(self):
        startTime = time.time()

        resumeHeader, filesize = None, self.getFilesize()
        if 0 < filesize:
            resumeHeader = {'Range': 'bytes={}-'.format(filesize)}

        if resumeHeader:
            self.logger.debug('Resume downloading {} from size {}'.format(self.filename, filesize))
            r, mode = requests.get(self.url, headers=resumeHeader, stream=True), 'ab'
        else:
            self.logger.debug('Start downloading {} from size 0'.format(self.filename))
            r, mode = requests.get(self.url, stream=True), 'wb'
        with open(self.filename, mode) as f:
            for chunk in r.iter_content(chunk_size=self.CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

        elapsedTime = time.time() - startTime
        self.logger.debug('Downloading {} completed'.format(self.filename))
        self.logger.debug('Elapsed time {0:.2f} sec'.format(elapsedTime))


#   https://gist.github.com/hyunjun/11f8c7ee9d5a5c4dd2804071dd4f5ab2#file-ftp-md
class FtpDownloader(Downloader):
    def __init__(self, url, port=21, path=None, filename=None, user='anonymous', password='anonymous'):
        super(self.__class__, self).__init__(url, port, path, filename, user, password)

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
    #    if self.path:
    #        self.ftp.cwd(self.path)
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

        if self.path:
            ftpAddr = '{}:{}/{}/{}'.format(self.url, self.port, self.path, self.filename)
        else:
            ftpAddr = '{}:{}/{}'.format(self.url, self.port, self.filename)
        resp = self.s.get(ftpAddr, auth=(self.user, self.password))
        if resp.status_code == requests.codes.ok:
            with open(self.filename, 'wb') as f:
                f.write(resp.content)

        elapsedTime = time.time() - startTime
        self.logger.debug('Downloading {} completed'.format(self.filename))
        self.logger.debug('Elapsed time {0:.2f} sec'.format(elapsedTime))


#   https://gist.github.com/hyunjun/11f8c7ee9d5a5c4dd2804071dd4f5ab2#file-sftp-md
class SftpDownloader(Downloader):
    def __init__(self, url, port=22, path=None, filename=None, user='anonymous', password='anonymous'):
        super(self.__class__, self).__init__(url, port, path, filename, user, password)

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
        self.client.connect(self.parsedUrl.netloc, port=self.port, username=self.user, password=self.password)
        sftp = self.client.open_sftp()
        if self.path:
            sftp.chdir(self.path)
        sftp.get(self.filename, self.filename)
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
    http_parser.set_defaults(command=Protocol.HTTP)

    ftp_parser = subparsers.add_parser(Protocol.FTP, help='Download file from (s)ftp address')
    ftp_parser.add_argument(Item.URL, action='store', help='Ftp address to download file')
    ftp_parser.add_argument('--port', action='store', dest=Item.PORT, default=21)
    ftp_parser.add_argument('--path', action='store', dest=Item.PATH, default=None)
    ftp_parser.add_argument('--filename', action='store', dest=Item.FILENAME, default=None)
    ftp_parser.add_argument('--user', action='store', dest=Item.USER, default='anonymous')
    ftp_parser.add_argument('--password', action='store', dest=Item.PASSWORD, default='anonymous')
    ftp_parser.set_defaults(command=Protocol.FTP)

    file_parser = subparsers.add_parser(FILE, help='Download file from configuration file')
    file_parser.add_argument(Item.FILENAME, action='store', help='Configuration file name')
    file_parser.set_defaults(command=FILE)

    option = parser.parse_args(argv[1:])
    return option


def foo(a, b):
    return a + b


if __name__ == '__main__':
    option, items = options(sys.argv), []
    if option.command is None:
        print("Execute with '--help' to see how to use")
        sys.exit(1)

    #   create log directory if it does NOT exist
    try:
        os.listdir(LOG_PATH)
    except FileNotFoundError:
        os.mkdir(LOG_PATH)

    print(option)
    #   python3 downloader.py http https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png
    if Protocol.HTTP == option.command:
        items.append({Item.URL: option.url})

    #   python3 downloader.py ftp ftp://demo.wftpserver.com --path download --filename manual_en.pdf --user demo-user --password demo-user
    #   python3 downloader.py ftp sftp://demo.wftpserver.com --port 2222 --path download --filename manual_en.pdf --user demo-user --password demo-user
    elif Protocol.FTP == option.command:
        items.append({Item.URL: option.url, Item.PORT: option.port, Item.PATH: option.path, Item.FILENAME: option.filename, Item.USER: option.user, Item.PASSWORD: option.password})

    #   python3 downloader.py file urls.dat
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
