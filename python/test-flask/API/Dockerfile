FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir /app
COPY ./api_only_flask.py /app
COPY ./requirements.txt /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["api_only_flask.py"]
