from concurrent.futures import ALL_COMPLETED
import aiohttp
import asyncio
import logging
import sys


async def url2json3(logger, url):
  try:
    response = await aiohttp.request('GET', url)
  except:
    return '{} unresponsive'.format(url)
  assert response.status == 200
  # result = await response.json()  # for json
  result = await response.text()
  response.close()
  return result


async def get_system_tagged3(logger, urls):
  futures = [url2json3(logger, url) for url in urls]
  done, pending = await asyncio.wait(futures, timeout=1, return_when=ALL_COMPLETED)
  for future in pending:
    future.cancel()
  responses = []
  for future in done:
    responses.append(future.result())
  return responses


if __name__ == '__main__':
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  ch = logging.StreamHandler(sys.stdout)
  ch = logging.NullHandler()
  logger.addHandler(ch)

  urls = ['http://daum.net', 'http://naver.com', 'http://google.com']

  result = []
  event_loop = asyncio.get_event_loop()
  try:
    result = event_loop.run_until_complete(get_system_tagged3(logger, urls))
  except:
    event_loop.close()
  for url, r in zip(urls, result):
    print('=' * 50)
    print(url)
    print('-' * 50)
    print(r)
