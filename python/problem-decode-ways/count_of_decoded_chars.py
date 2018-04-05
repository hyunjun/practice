

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

inp = '23#(2)24#2(2)25#126#23#(3)'  #   wwxbbyazwww
print(count_of_decoded_chars(inp))
inp = '2'   #   b
inp = '2(2)'   #   b
inp = '10#'   #   b
inp = '10#(2)'   #   b
print(count_of_decoded_chars(inp))
