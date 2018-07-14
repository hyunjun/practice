#   https://leetcode.com/problems/decode-ways
#   http://www.glassdoor.com/Interview/I-was-given-a-question-about-decoding-which-means-decoding-a-message-with-a-mapping-between-number-and-character-Actuall-QTN_559036.htm
#   https://www.youtube.com/watch?v=qli-JCrSwuk


def numOfDecodes(s):
    if s is None or len(s) == 0:
        return 0

    res = [0] * len(s)
    for i, c in enumerate(s):
        if 0 == i:
            if '1' <= c <= '9':
                res[i] = 1
        elif 1 == i:
            if '1' <= c <= '9':
                res[i] += res[i - 1]
            if '10' <= s[:i + 1] <= '26':
                res[i] += 1
        else:
            if '1' <= c <= '9':
                res[i] += res[i - 1]
            if '10' <= s[i - 1:i + 1] <= '26':
                res[i] += res[i - 2]
    return res[-1]


from data import cases
for msg, expected in cases:
    real = numOfDecodes(msg)
    print('{}\texpected {}\treal {}\tresult {}'.format(msg, expected, real, expected == real))
