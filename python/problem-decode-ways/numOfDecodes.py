#   https://leetcode.com/problems/decode-ways
#   http://www.glassdoor.com/Interview/I-was-given-a-question-about-decoding-which-means-decoding-a-message-with-a-mapping-between-number-and-character-Actuall-QTN_559036.htm


#   Wrong Answer
def numOfDecodes(str):
    if str is None or len(str) == 0:
        return 0

    if 1 == len(str):
        if '0' == str[:1]:
            return 0
        return 1
    if 2 == len(str):
        if '0' == str[:1]:
            return numOfDecodes(str[1:])
        if '1' == str[:1]:
            if '0' == str[1:]:
                return 1
            return 2
        if '2' == str[:1]:
            if '0' == str[1:] or '7' <= str[1:]:
                return 1
            return 2
        return 1
    return numOfDecodes(str[1:]) + numOfDecodes(str[2:])


from decode_ways import cases
for msg, expected in cases:
    real = numOfDecodes(msg)
    print('{}\texpected {}\treal {}\tresult {}'.format(msg, expected, real, expected == real))
