import memory_profiler
import requests


@memory_profiler.profile
def download(url, filepath):
    r = requests.get(url, stream=True)
    f = open(filepath, 'wb')
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
    f.close()


url, filepath = 'http://speedtest.ftp.otenet.gr/files/test100Mb.db', '/tmp/test100Mb.db'
download(url, filepath)
