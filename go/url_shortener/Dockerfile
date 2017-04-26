FROM golang

RUN useradd -r -s /bin/false helloworld

ENV GOBIN /go/bin
ADD ./src/url_shortener.go /go/src
RUN go install /go/src/url_shortener.go

ENTRYPOINT /go/bin/url_shortener

EXPOSE 8889
