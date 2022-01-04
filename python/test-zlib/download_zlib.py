import memory_profiler
import requests
import zlib


@memory_profiler.profile
def download(url, filepath):
    zipfilepath = filepath + '.zip'
    r = requests.get(url, stream=True)
    compressor = zlib.compressobj()
    with open(zipfilepath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(compressor.compress(chunk))
        f.write(compressor.flush())

    with open(zipfilepath, 'rb') as rf:
        d = rf.read()
        data = zlib.decompress(d)
        with open(filepath, 'wb') as f:
            f.write(data)


url, filepath = 'http://speedtest.ftp.otenet.gr/files/test100Mb.db', '/tmp/test100Mb.zlib.db'
download(url, filepath)
