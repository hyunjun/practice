test-pyev
=========
* usage

  ```
  $ LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH python test_pyev_server.py
  $ python test_pyev_client.py test
  test received
  ```
*dha_ install
  * [libev](http://software.schmorp.de/pkg/libev.html)

    ```
    $ wget http://dist.schmorp.de/libev/libev-4.19.tar.gz
    $ tar xvfz libev-4.19.tar.gz
    $ cd libev-4.19
    $ ./configure # default installation into /usr/local/lib
    $ make && make install
    ```
  * [pyev](https://pypi.python.org/pypi/pyev/)

    ```
    $ wget https://pypi.python.org/packages/source/p/pyev/pyev-0.9.0.tar.gz#md5=9d7466c84c4fc57a5d2f02d89da82b7b
    $ tar xvfz pyev-0.9.0.tar.gz
    $ cd pyev-0.9.0
    $ LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH python setup.py install 
    $ LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH python -c 'import pyev'
    ```
