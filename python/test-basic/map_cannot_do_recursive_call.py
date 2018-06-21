print('\nbasic recursive call')
def foo(prev, n):
    if n == 0:
        return
    print('Start - prev {} n {}'.format(prev, n))
    for i in range(n - 1, 0, -1):
        foo(prev, i)
    print('  End - prev {} n {}'.format(prev, n))

[foo(i, i) for i in range(3, 0, -1)]

print('\nmap; recursive call NOT work')
def bar(prev, n):
    if n == 0:
        return
    print('Start - prev {} n {}'.format(prev, n))
    map(bar, [(prev, i) for i in range(n - 1, 0, -1)])
    print('  End - prev {} n {}'.format(prev, n))

[bar(i, i) for i in range(3, 0, -1)]
