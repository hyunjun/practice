#   http://hamait.tistory.com/834
import asyncio


@asyncio.coroutine
def A():
    raise Exception('Something went wrong in A!')


@asyncio.coroutine
def B():
    a = yield from A()
    yield a + 1


@asyncio.coroutine
def C():
    try:
        b = yield from B()
        print(b)
    except Exception as e:
        print('C got exception: {}'.format(e))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(C())


if __name__ == '__main__':
    main()
