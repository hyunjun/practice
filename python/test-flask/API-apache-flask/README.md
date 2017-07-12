# Debian - Flask + Mod_Wsgi API

* Original repo; [https://github.com/Craicerjack/apache-flask](https://github.com/Craicerjack/apache-flask)
* Execution
  ```
  $ docker run --env-file=app/config.env --rm -p 80:80 --name test-apache-flask apache-flask

  $ curl http://localhost
  Welcome

  $ curl http://localhost/count
  count

  $ curl http://localhost/select/123
  select id 123

  $ curl http://localhost/delete/123
  delete id 123

  $ curl -XPUT http://localhost/insert/123 -F sentence="값"
  insert id 123 값

  $ curl http://localhost/stop
  stop
  ```
* Installation
  * `docker build -t apache-flask:latest .`
  * `docker build -f Dockerfile3 -t apache-flask:latest .` for python3 on debian
    * [Getting Flask to use Python3 (Apache/mod_wsgi)](https://stackoverflow.com/questions/30642894/getting-flask-to-use-python3-apache-mod-wsgi)
  * `docker build -f Dockerfile3.ubuntu -t apache-flask:latest .` for python3 on ubuntu
    * Compare [apache-flask3.wsgi](apache-flask3.wsgi) (for debian) vs. [apache-flask3.ubuntu.wsgi](apache-flask3.ubuntu.wsgi) (for ubuntu)
      * Without modifying wsgi file like apache-flask3.wsgi, error occurs. see details at [error.log](error.log)
    * [python3-mod_wsgi: site.addsitedir() fails if multiple directories in python-path](https://bugzilla.redhat.com/show_bug.cgi?id=1345725)
