'''
cases
1~9 a~i
    1~9다음에 숫자가 바로 나온다면 a~i 한 글자
    숫자 숫자 괄호 아님
1~9 + (n)   a~i * n
    1~9다음에 괄호가 나온다면 a~i n 글자
    숫자 괄호
10#~26# j~z
    1~9다음에 숫자# + 숫자가 나온다면 j~z 한 글자
    숫자 숫자 # 숫자
10#~26# + (n)   j~z * n
    1~9다음에 숫자# + 괄호가 나온다면 j~z n 글자
    숫자 숫자 # 괄호

즉 입력의 현재 index i에서 최소 +1~+3까지 살펴봐야 어느 case인지 확정

일단 바로 종료하는 case를 살펴보면
1~9
1~9(n)
10#~26#
10#~26#(n)
'''


def count_of_decoded_chars(inp):
    result = [0] * 26

    i = 0
    while i < len(inp):
        if inp[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('0')
            if i + 1 < len(inp):
                print('1')
                #   1~9 + (n), 즉 a~i n번 반복
                if inp[i + 1] == '(':
                    char_idx = int(inp[i]) - 1
                    result[char_idx] += int(inp[i + 2])
                    i += 4
                elif i + 2 < len(inp) and inp[i + 2] == '#':
                    char_idx = int(inp[i:i + 2]) - 1
                    #   10#~26# + (n), 즉 j~z n번 반복
                    if i + 3 < len(inp) and inp[i + 3] == '(':
                        result[char_idx] += int(inp[i + 4])
                        i += 6
                    #   10#~26#, 즉 j~z 1번
                    else:
                        result[char_idx] += 1
                        i += 3
                else:
                    print('2')
                    char_idx = int(inp[i]) - 1
                    result[char_idx] += 1
                    i += 1
                continue
        i += 1
    return result


#inp = '23#(2)24#2(2)25#126#23#(3)'  #   wwxbbyazwww
#[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 1]
#print(count_of_decoded_chars(inp))
#inp = '2'   #   b
#[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#inp = '2(2)'   #   bb
#[0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#inp = '10#'   #   j
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#inp = '10#(2)'   #   jj
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#print(count_of_decoded_chars(inp))


class Solution:
    def countOfEncodedChars(self, inp):
        result = [0] * 26
        idx = len(inp) - 1
        while -1 < idx:
            cnt = 1
            if ')' == inp[idx]:
                openIdx = idx - 1
                while -1 < openIdx and '(' != inp[openIdx]:
                    openIdx -= 1
                cnt = int(inp[openIdx + 1:idx])
                idx = openIdx - 1
            if '#' == inp[idx]:
                charIdx = int(inp[idx - 2:idx]) - 1
                idx -= 3
            else:
                charIdx = int(inp[idx]) - 1
                idx -= 1
            result[charIdx] += cnt
        return result

    def count2chars(self, inp):
        return ' '.join(['{}{}'.format(chr(i + 97), n) for i, n in enumerate(inp) if 0 < n])


s = Solution()
        # ww    x  bb  y  az  www
data = [('23#(2)24#2(2)25#126#23#(3)', [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 1]),
        # b
        ('2', [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        # bb
        ('2(2)', [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        # j
        ('10#', [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        # jj
        ('10#(2)', [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ]
for inp, expected in data:
    real = s.countOfEncodedChars(inp)
    strAndCount = s.count2chars(real)
    print('{}, {}, result {}'.format(inp, strAndCount, expected == real))
    print(real)
