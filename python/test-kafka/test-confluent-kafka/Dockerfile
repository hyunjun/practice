FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential locales wget
#software-properties-common 
#RUN add-apt-repository "deb http://cz.archive.ubuntu.com/ubuntu xenial-updates main"
#RUN apt-get dist-upgrade -y
#RUN apt-get install -y wget apt-transport-https
#RUN wget -qO - https://packages.confluent.io/deb/4.0/archive.key | apt-key add -
#RUN add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/4.0 stable main"
#RUN apt-get install -y confluent-platform-oss-2.11 librdkafka-dev
#RUN apt-get install -y librdkafka-dev

# without python soft link, cannot configure librdkafka
RUN ln -sf /usr/bin/python3 /usr/bin/python

ARG BUILD_DIR=/tmp
ARG LIBRDKAFKA_NAME="librdkafka"
#ARG LIBRDKAFKA_VER="0.9.1"
ARG LIBRDKAFKA_VER="v0.11.3"

#	without ldconfig
#	ImportError: librdkafka.so.1: cannot open shared object file: No such file or directory
#	https://github.com/confluentinc/confluent-kafka-python/issues/65
RUN wget -O "$BUILD_DIR/$LIBRDKAFKA_NAME.tar.gz" "https://github.com/edenhill/librdkafka/archive/$LIBRDKAFKA_VER.tar.gz" && \
    mkdir -p $BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER && \
    tar \
      --extract \
      --file "$BUILD_DIR/$LIBRDKAFKA_NAME.tar.gz" \
      --directory "$BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER" \
      --strip-components 1 && \
    cd $BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER && \
    ./configure && make && make install && ldconfig && \
    rm -rf $BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER

RUN mkdir /app
COPY ./test.py /app/test.py
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYTHONIOENCODING="utf-8"

RUN locale-gen ko_KR.UTF-8

ENV LANG=ko_KR.UTF-8
ENV LANGUAGE=ko_KR.UTF-8
ENV LC_ALL=ko_KR.UTF-8
#ENV LC_CTYPE=ko_KR.UTF-8

ENTRYPOINT ["python3"]
CMD ["test.py"]
