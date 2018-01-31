import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print('Task {}: Compute factorial({})...'.format(name, i))
        await asyncio.sleep(1)
        f *= i
    print('Task {}: factorial({}) = {}'.format(name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial('A', 2),
    factorial('B', 3),
    factorial('C', 4),
))
loop.close()
