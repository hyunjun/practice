
def atof(s):
    c = 'e'
    if 'E' in s:    c = 'E'
    l = s.split(c)
    f = float(l[0])
    n = int(l[1][1:])
    if l[1][:1] == '+':
        while n > 0:
            f *= 10
            n -= 1
    else:
        while n > 0:
            f /= 10
            n -= 1
    return f

if __name__ == '__main__':
    print(atof('2.4e-1'))
    print(atof('2.4E+1'))
