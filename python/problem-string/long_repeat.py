#   https://py.checkio.org/mission/long-repeat

#   https://py.checkio.org/mission/long-repeat/publications/tom-tom/python-3/first/?ordering=most_voted&filtering=all
#   return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    start, maxLen = 0, 0
    for i, c in enumerate(line):
        if 0 == i:
            continue
        elif line[i - 1] != c:
            maxLen = max(maxLen, i - start)
            start = i
    maxLen = max(maxLen, len(line) - start)
    return maxLen

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
