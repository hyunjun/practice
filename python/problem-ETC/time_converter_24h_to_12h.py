#   https://py.checkio.org/mission/time-converter-24h-to-12h


def time_converter(time):
    hh, mm = time.split(':')
    hhNum, mmNum = int(hh), int(mm)
    if 0 == hhNum and 0 == mmNum:
        return '12:{} a.m.'.format(mm)
    if hhNum <= 11 and mmNum <= 59:
        return '{}:{} a.m.'.format(hhNum, mm)
    if 12 == hhNum:
        return '{}:{} p.m.'.format(hhNum, mm)
    return '{}:{} p.m.'.format(hhNum - 12, mm)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
