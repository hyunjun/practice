# Downloader

* A file downloader which downloads it from http(s) or (s)ftp url
* Installation

  ```
  $ pip install virtualenv
  $ python3 -m virtualenv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
* Test `python3 test_downloader.py`
* Execution

  ```
  $ python3 downloader.py http https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png [--local-path from_http]
  $ python3 downloader.py ftp ftp://demo.wftpserver.com --path download --filename manual_en.pdf --user demo-user --password demo-user [--local-path from_ftp]
  $ python3 downloader.py ftp sftp://demo.wftpserver.com --port 2222 --path download --filename manual_en.pdf --user demo-user --password demo-user [--local-path from_sftp]
  $ python3 downloader.py file urls.dat
  ```
