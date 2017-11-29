FROM ubuntu:latest

#RUN apt-get update && apt-get install -y build-essential python3 python3-dev python3-pip
RUN apt-get update && apt-get install -y python3

#RUN pip3 install --upgrade pip
#RUN pip3 install -U memory_profiler

RUN mkdir /test/
RUN mkdir /logs
COPY ./* /test/

WORKDIR "/test"

ENV PYTHONIOENCODING="utf-8"
ENV LANG=ko_KR.UTF-8
ENV LANGUAGE=ko_KR.UTF-8
ENV LC_ALL=ko_KR.UTF-8
