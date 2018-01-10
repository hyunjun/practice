#!/bin/sh
#docker build -f Dockerfile --build-arg http_proxy=http://x.y.z.w:port --build-arg https_proxy=http://x.y.z.w:port -t leak_test:latest .
docker build -f Dockerfile -t leak_test:latest .
docker run --rm -it -m 32m -v `pwd`/log:/logs leak_test:latest bash
