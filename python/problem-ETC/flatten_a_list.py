#   https://py.checkio.org/en/mission/flatten-list

#   https://py.checkio.org/mission/flatten-list/publications/DiZ/python-3/60/?ordering=most_voted&filtering=all
#   flat_list=f=lambda d:[d]if int==type(d)else sum(map(f,d),[])

def flat_list(array):
    ret = []
    for i, a in enumerate(array):
        if isinstance(a, list):
            ret.extend(flat_list(a))
        else:
            ret.append(a)
    return ret


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
