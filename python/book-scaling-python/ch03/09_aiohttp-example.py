import aiohttp
import asyncio


#   'async with' is the same as 'await' except that await is used between __enter__ and __exit__ (inside of context manager)
async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


loop = asyncio.get_event_loop()
coroutines = [get('http://example.com') for _ in range(8)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
print('Results: {}'.format(results))
