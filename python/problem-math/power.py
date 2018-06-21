
def power(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1

    res = 1.0
    exp = abs(exponent)
    while exp > 0:
        res *= base
        exp -= 1
    
    if exponent < 0:
        return 1 / res
    return res

def power2(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1

    res = power_r(base, abs(exponent))
    
    if exponent < 0:
        return 1 / res
    return res

def power_r(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    res = power_r(base, exponent >> 1)
    res *= res
    if exponent & 0x1 == 1:
        res *= base
    return res

if __name__ == '__main__':
    print(power(0, 10))
    print(power(2, 0))
    print(power(2, 3))
    print(power(2, -3))
    print(power(4, 3))
    print(power(8, -3))
    print(power2(4, 3))
    print(power2(8, -3))
