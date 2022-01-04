import memory_profiler
import requests
import zlib


@memory_profiler.profile
def download(url, filepath):
    zipfilepath = filepath + '.zip'
    r = requests.get(url, stream=True)
    f, compressor = open(zipfilepath, 'wb'), zlib.compressobj()
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(compressor.compress(chunk))
    f.write(compressor.flush())
    f.close()

    f = open(zipfilepath, 'rb')
    d = f.read()
    f.close()

    data = zlib.decompress(d)
    f = open(filepath, 'wb')
    f.write(data)
    f.close()


url, filepath = 'http://speedtest.ftp.otenet.gr/files/test100Mb.db', '/tmp/test100Mb.zlib.db'
download(url, filepath)
