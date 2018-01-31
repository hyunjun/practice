#   http://hamait.tistory.com/834
import asyncio
import json


host = 'api.ipify.org'
request_headers = {'User-Agent': 'python/3.4',
                   'Host': host,
                   'Accept': 'application/json',
                   'Accept-Charset': 'UTF-8'}


@asyncio.coroutine
def write_headers(writer):
    for key, value in request_headers.items():
        writer.write((key + ': ' + value + '\r\n').encode())
    writer.write(b'\r\n')
    yield from writer.drain()


@asyncio.coroutine
def read_headers(reader):
    response_headers = {}
    while True:
        line_bytes = yield from reader.readline()
        line = line_bytes.decode().strip()
        if not line:
            break
        key, value = line.split(':', 1)
        response_headers[key.strip()] = value.strip()
    return response_headers


@asyncio.coroutine
def get_my_ip_address(verbose):
    reader, writer = yield from asyncio.open_connection(host, 80)
    writer.write(b'GET /?format=json HTTP/1.1\r\n')
    yield from write_headers(writer)
    status_line = yield from reader.readline()
    status_line = status_line.decode().strip()
    http_version, status_code, status = status_line.split(' ')
    if verbose:
        print('Got status {} {]'.format(status_code, status))
    response_headers = yield from read_headers(reader)
    if verbose:
        print('Response headers:')
        for key, value in response_headers.items():
            print(key + ': ' + value)
    content_length = int(response_headers['Content-Length'])
    response_body_bytes = yield from reader.read(content_length)
    response_body = response_body_bytes.decode()
    response_boject = json.loads(response_body)
    writer.close()
    return response_object['ip']


@asyncio.coroutine
def print_my_ip_address(verbose):
    try:
        ip_address = yield from get_my_ip_address(verbose)
        print('My IP address is:')
        print(ip_address)
    except Exception as e:
        print('Error: {}'.format(str(e)))


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(print_my_ip_address(verbose=True))
    finally:
        loop.close()


if __name__ == '__main__':
    main()
