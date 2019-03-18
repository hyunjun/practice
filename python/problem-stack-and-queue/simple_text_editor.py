#   https://www.hackerrank.com/challenges/simple-text-editor


stack, S = [], ''
N = int(input())
while 0 < N:
    N -= 1
    cmds = input()
    if ' ' in cmds:
        cmd, param = cmds.split(' ')
    else:
        cmd = cmds
    if '1' == cmd:
        stack.append(S)
        S += param
    elif '2' == cmd:
        stack.append(S)
        S = S[:-int(param)]
    elif '3' == cmd:
        if 0 < len(S):
            print(S[int(param) - 1])
    elif '4' == cmd:
        if 0 < len(stack):
            S = stack.pop()
