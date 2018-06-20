
def isMatching(src, reg):
    if len(src) == 0 or len(reg) == 0:
        if len(src) == len(reg):
            return  True
        else:
            return  False

    if len(reg) >= 2 and reg[1:2] == '*':
        for n in range(len(src)):
            subResult = isMatching(src, reg[:1] * n + reg[2:])
            if subResult:
                return  True
    else:
        if reg[:1] == '.' or src[:1] == reg[:1]:
            return  isMatching(src[1:], reg[1:])
    return  False

if __name__ == '__main__':
    src = 'aaa'
    regs = [ 'a.a', 'ab*ac*a', 'aa.a', 'ab*a' ]
    for reg in regs:
        print(src, reg, isMatching(src, reg))
