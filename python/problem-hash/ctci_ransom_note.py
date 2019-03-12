#   https://www.hackerrank.com/challenges/ctci-ransom-note


from collections import Counter

def checkMagazine(magazine, note):
    m, n = Counter(magazine), Counter(note)
    for word, cnt in n.items():
        if word not in m or m[word] < cnt:
            return 'No'
    return 'Yes'


data = [('give me one grand today night', 'give one grand today', 'Yes'),
        ('two times three is not four', 'two times two is four', 'No'),
        ('ive got a lovely bunch of coconuts', 'ive got some coconuts', 'No'),
        ]
for magazine, note, expected in data:
    real = checkMagazine(magazine, note)
    print('{}, {}, expected {}, real {}, result {}'.format(magazine, note, expected, real, expected == real))
