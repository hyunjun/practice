def save(func, i):
    def decorator(*args, **kargs):
        if i:
            res = func(*args) + i
        elif False:
            assert False
            #i = 1
        else:
            print('2')
            res = func(*args) + 1

        return res

    return decorator

def f(a,b,c):
    return a+b+c

if __name__ == '__main__':
    print(save(f, 2)(1,2,3))
