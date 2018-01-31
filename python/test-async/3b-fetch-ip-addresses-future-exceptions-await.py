from collections import namedtuple
import time
import asyncio
import async_timeout
import aiohttp
import traceback

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'this-is-not-an-attr'),
    Service('broken', 'http://no-way-this-is-going-to-work.com/json', 'ip')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    try:
        with async_timeout.timeout(1):
            response = await aiohttp.request('GET', service.url)
    except:
        return '{} is unresponsive'.format(service.name)

    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, _ = await asyncio.wait(futures)

    for future in done:
        try:
            print(future.result())
        except:
            print("Unexpected error: {}".format(traceback.format_exc()))


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
