#   https://www.hackerrank.com/challenges/caesar-cipher-1


def caesarCipher(s, k):
    if s is None or 0 == len(s) or 0 == k:
        return s
    l = list(s)
    for i, c in enumerate(l):
        n = ord(c)
        if 'a' <= c <= 'z':
            n = (ord(c) - ord('a') + k) % 26 + ord('a')
        elif 'A' <= c <= 'Z':
            n = (ord(c) - ord('A') + k) % 26 + ord('A')
        l[i] = chr(n)
    return ''.join(l)


data = [('middle-Outz', 2, 'okffng-Qwvb'),
        ('Always-Look-on-the-Bright-Side-of-Life', 5, 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'),
        ]
for s, k, expected in data:
    real = caesarCipher(s, k)
    print('{}, {}, expected {}, real {}, result {}'.format(s, k, expected, real, expected == real))
