#   https://www.hackerrank.com/challenges/sherlock-and-valid-string


from collections import Counter

def isValid(s):
    if s is None or 0 == len(s):
        return 'NO'
    counter = Counter(s)
    counterValues = set(counter.values())
    numValues = len(counterValues)
    if 1 == numValues:
        return 'YES'
    if 2 != numValues:
        return 'NO'
    a, b = min(list(counterValues)), max(list(counterValues))
    #if 1 != abs(a - b):
    #    return 'NO'
    d = {a: [], b: []}
    for c, cnt in counter.items():
        d[cnt].append(c)
    '''
    if 1 == len(d[a]):
        counter[d[a][0]] -= 1
        if 1 == len(set(counter.values())):
            return 'YES'
        counter[d[a][0]] += 1
    if 1 == len(d[b]):
        counter[d[b][0]] -= 1
        if 1 == len(set(counter.values())):
            return 'YES'
        counter[d[b][0]] += 1
    return 'NO'
    '''
    #if 1 != len(d[a]) and 1 != len(d[b]):
    #    return 'NO'
    #return 'YES'
    '''
    for c in s:
        counter[c] -= 1
        if 1 == len(set(counter.values())):
            return 'YES'
        counter[c] += 1
    return 'NO'
    '''
    if (1 == a and 1 == len(d[a])) or (a + 1 == b and 1 == len(d[b])):
        return 'YES'
    return 'NO'


data = [('aabbcd', 'NO'),
        ('aabbccddeefghi', 'NO'),
        ('abcdefghhgfedecba', 'YES'),
        ('abcdefghhgfedcba', 'YES'),
        ('', 'NO'),
        ]
for s, expected in data:
    real = isValid(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
