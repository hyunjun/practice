#   http://hamait.tistory.com/834
import asyncio
import random


async def get_url(url):
    wait_time = random.randint(1, 4)
    await asyncio.sleep(wait_time)
    print('Done: URL {} took {}s to get!'.format(url, wait_time))
    return url, wait_time


async def process_as_results_come_in():
    coroutines = [get_url(url) for url in ['URL1', 'URL2', 'URL3']]
    for coroutine in asyncio.as_completed(coroutines):
        url, wait_time = await coroutine
        print('Coroutine for {} is done'.format(url))


async def process_once_everything_ready():
    coroutines = [get_url(url) for url in ['URL1', 'URL2', 'URL3']]
    results = await asyncio.gather(*coroutines)
    print(results)


def main():
    loop = asyncio.get_event_loop()
    print('First, process results as they come in:')
    loop.run_until_complete(process_as_results_come_in())
    print('\nNow, process results once they are all ready:')
    loop.run_until_complete(process_once_everything_ready())


if __name__ == '__main__':
    main()
