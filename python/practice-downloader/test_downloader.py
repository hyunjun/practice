from unittest import TestCase
from unittest import main
import os
import shutil
import sys


sys.path.append(os.path.join(os.path.dirname('.')))


import downloader


downloader.mkdirIfNotExist(downloader.LOG_PATH)


class TestUtility(TestCase):

    def testMkdir(self):
        testPathname = 'tmp_dir'

        dirs = os.listdir('.')
        self.assertFalse(testPathname in dirs)

        downloader.mkdirIfNotExist(testPathname)

        dirs = os.listdir('.')
        self.assertTrue(testPathname in dirs)

        os.rmdir(testPathname)

    def testGetFilename(self):
        self.assertIsNone(downloader.getFilename(None))
        self.assertEqual('filename', downloader.getFilename('filename'))
        self.assertEqual('filename', downloader.getFilename('/filename'))
        self.assertEqual('filename', downloader.getFilename('http://something.com/path/filename'))


class TestHttpDownloader(TestCase):

    def setUp(self):
        self.url = 'https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png'
        self.local = 'from_http'
        dirs = os.listdir('.')
        if self.local in dirs:
            shutil.rmtree(self.local)
        self.expectedFilesize = 11065

    #   Download to current directory
    def testDownload0(self):
        item = {downloader.Item.URL: self.url}
        d = downloader.Downloader.factory(item)
        try:
            os.remove(d.filename)
        except FileNotFoundError:
            pass
        if d:
            d.download()
        with open(d.filename) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())

        #   Continuous download, an existing file is 3128 bytes
        partialFilename = '{}.https_downloading'.format(d.filename)
        with open(partialFilename, 'wb') as dst:
            with open(d.filename, 'rb') as src:
                dst.write(src.read(3128))
        d = downloader.Downloader.factory(item)
        if d:
            d.download()
        with open(d.filename) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())

        os.remove(d.filename)

    #   Download to specific local directory
    def testDownload1(self):
        item = {downloader.Item.URL: self.url, downloader.Item.LOCAL_PATH: self.local}
        d = downloader.Downloader.factory(item)
        if d:
            d.download()
        with open(os.path.join(d.local, d.filename)) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())
        shutil.rmtree(d.local)


class TestFtpDownloader(TestCase):

    def setUp(self):
        self.url = 'ftp://demo.wftpserver.com'
        self.remote = 'download'
        self.filename = 'manual_en.pdf'
        self.local = 'from_ftp'
        self.user = 'demo-user'
        self.password = 'demo-user'
        dirs = os.listdir('.')
        if self.local in dirs:
            shutil.rmtree(self.local)
        self.expectedFilesize = 10187202

    #   Download to current directory
    def testDownload0(self):
        item = {downloader.Item.URL: self.url, downloader.Item.REMOTE_PATH: self.remote, downloader.Item.FILENAME: self.filename, downloader.Item.USER: self.user, downloader.Item.PASSWORD: self.password}
        d = downloader.Downloader.factory(item)
        try:
            os.remove(d.filename)
        except FileNotFoundError:
            pass
        if d:
            d.download()
        with open(d.filename) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())
        os.remove(d.filename)

    #   Download to specific local directory
    def testDownload1(self):
        item = {downloader.Item.URL: self.url, downloader.Item.REMOTE_PATH: self.remote, downloader.Item.FILENAME: self.filename, downloader.Item.LOCAL_PATH: self.local, downloader.Item.USER: self.user, downloader.Item.PASSWORD: self.password}
        d = downloader.Downloader.factory(item)
        if d:
            d.download()
        with open(os.path.join(d.local, d.filename)) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())
        shutil.rmtree(d.local)


class TestSftpDownloader(TestCase):

    def setUp(self):
        self.url = 'sftp://demo.wftpserver.com'
        self.port = 2222
        self.remote = 'download'
        self.filename = 'manual_en.pdf'
        self.local = 'from_sftp'
        self.user = 'demo-user'
        self.password = 'demo-user'
        dirs = os.listdir('.')
        if self.local in dirs:
            shutil.rmtree(self.local)
        self.expectedFilesize = 10187202

    #   Download to current directory
    def testDownload0(self):
        item = {downloader.Item.URL: self.url, downloader.Item.PORT: self.port, downloader.Item.REMOTE_PATH: self.remote, downloader.Item.FILENAME: self.filename, downloader.Item.USER: self.user, downloader.Item.PASSWORD: self.password}
        d = downloader.Downloader.factory(item)
        try:
            os.remove(d.filename)
        except FileNotFoundError:
            pass
        if d:
            d.download()
        with open(d.filename) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())
        os.remove(d.filename)

    #   Download to specific local directory
    def testDownload1(self):
        item = {downloader.Item.URL: self.url, downloader.Item.PORT: self.port, downloader.Item.REMOTE_PATH: self.remote, downloader.Item.FILENAME: self.filename, downloader.Item.LOCAL_PATH: self.local, downloader.Item.USER: self.user, downloader.Item.PASSWORD: self.password}
        d = downloader.Downloader.factory(item)
        if d:
            d.download()
        with open(os.path.join(d.local, d.filename)) as f:
            f.seek(0, os.SEEK_END)
            self.assertEqual(self.expectedFilesize, f.tell())
        shutil.rmtree(d.local)


if __name__ == '__main__':
    main()
