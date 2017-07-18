Flask API
=========

* Execution

  ```
  $ docker run --env-file=common/config/settings.env --rm -v `pwd`/logs:/app/logs -p 59459:5000 test-flask-api
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 236-035-556

  $ curl http://localhost:59459
  Welcome

  $ curl http://localhost:59459/count
  count

  $ curl http://localhost:59459/select/123
  select id 123

  $ curl http://localhost:59459/delete/123
  delete id 123

  $ curl -XPUT http://localhost:59459/insert/123 -F sentence="값"
  insert id 123 값

  $ curl http://localhost:59459/stop
  stop
  ```
* Installation

  ```
  $ docker build -f Dockerfile3 -t test-flask-api:latest .
  ```
