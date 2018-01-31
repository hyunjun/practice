#   http://hamait.tistory.com/834


def coroutine():
    print('Starting')
    try:
        yield "Let's pause until continued"
        print('Continuing')
    except Exception as e:
        yield 'Got an exception: {}'.format(str(e))


def main():
    c = coroutine()
    next(c) #   첫 번째 yield까지 실행
    value = c.throw(Exception('Have an exceptional day!'))
    print(value)


if __name__ == '__main__':
    main()
