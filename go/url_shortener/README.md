# URL Shortener

## Idea
* functions
  * cleaner; remove http(s)://www., tailing /(slash), etc.
  * validator; right url? existing url?
  * save the original url - the shortened url pairs into file, and read them from file
* flow
  * get the input url
  * is it valid? (validator function)
    * exit if no
  * clear it (cleaner)
  * check whether it exists in the dictionary which has the original url - the shortened url pairs
    * return the shortened url if it does
  * make the shortened url
  * check whether the shortened url has the same contents with the original one
    * return error if it is not the same
  * compare the length of them
    * return the original url if the shortened url is longer
  * return the shortened url
  * ![idea](images/20170413.png)

## Test
* Installation

  ```
  $ docker build -t url_shortener .
  Sending build context to Docker daemon 15.44 MB
  Step 1/7 : FROM golang
   ---> c0ccf5f2c036
  ...
  Successfully built ...
  $ docker run -p 8889:8889 --name test --rm url_shortener
  ```
* Test

  ```
  # get short
  $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/shorten' -d '{"url": "http://viki.com"}'
  {"short": "localhost/4193782667"}

  # The same connection using different input, with 'www.' returns the same short url
  $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/shorten' -d '{"url": "http://www.viki.com"}'
  {"short": "localhost/4193782667"}

  # get original
  $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/original' -d '{"url": "localhost/4193782667"}'
  {"original": "viki.com"}
  ```

## Progress (The upper items are latest, usually spent 30min ~ 1hour / day)
* 04.21
  * [Dockerfile](./Dockerfile) Dockerfile to run hello_webserver for test

    ```
    $ docker build -t url_shortener .
    ...
    Successfully built ...
    $ docker run -p 8889:8889 --name test --rm url_shortener

    $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/original' -d '{"url": "test original"}'
    {"url": "test original"}
    test original
    welcome to original function!
    $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/shorten' -d '{"url": "test shorten"}'
    {"url": "test shorten"}
    test shorten
    welcome to shorten function!
    ```
* 04.20
  * [hello_map](practice/hello_map.go)
    * map to json, and json back to map
    * map to json to file, and file back to map
  * [hello regexp](practice/hello_regex.go) capture group in regular expression
* 04.18
  * [hello regexp](practice/hello_regex.go) very simple url pattern matching
  * [hello webserver](practice/hello_webserver.go) add read & parse json

    ```
    $ go run hello_webserver.go

    # different terminal
    $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/shorten' -d '{"url": "test"}'
    {"url": "test shorten"}
    test shorten
    welcome to shorten function!
    $ curl -sX POST -H 'Content-Type: application/json' 'localhost:8889/original' -d '{"url": "test"}'
    {"url": "test original"}
    test original
    welcome to original function!
    ```
* 04.17
  * [hello webserver](practice/hello_webserver.go)
* 04.14
  * [hello_map](practice/hello_map.go) practice of map, array, for loop, and if-else
  * install go, set configurations in .bash_profile & .vimrc to run the [hello world](practice/hello_world.go)

    ```
    $ go version
    go version go1.8.1 darwin/amd64
    ```
* 04.13; create this repository, and write the first draft of the idea on README.md
