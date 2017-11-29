#!/bin/sh
#docker build -f Dockerfile --build-arg http_proxy=http://proxy.daumkakao.io:3128 --build-arg https_proxy=http://proxy.daumkakao.io:3128 -t leak_test:latest .
docker build -f Dockerfile -t leak_test:latest .
docker run --rm -it -m 32m -v `pwd`/log:/logs leak_test:latest bash
