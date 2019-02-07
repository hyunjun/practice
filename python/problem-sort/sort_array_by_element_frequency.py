#   https://py.checkio.org/en/mission/sort-array-by-element-frequency

#   https://py.checkio.org/mission/sort-array-by-element-frequency/publications/flpo/python-3/-itemscountx-itemsindexx/?ordering=most_voted&filtering=all
#   return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

def frequency_sort(items):
    d = {}
    for i, item in enumerate(items):
        if item in d:
            d[item] = (d[item][0] + 1, d[item][1])
        else:
            d[item] = (1, i)
    ret, sortedD = [], sorted(d.items(), key=lambda t: (-1 * t[1][0], t[1][1]))
    for item, t in sortedD:
        ret.extend([item] * t[0])
    return ret


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
