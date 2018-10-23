import asyncio


async def hello_world():
    print('hello world!')


async def hello_python():
    print('hello Python!')
    await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(asyncio.gather(hello_world(), hello_python(),))
    print(result)
finally:
    event_loop.close()
