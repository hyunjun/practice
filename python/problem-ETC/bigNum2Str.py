
def bigNum2Str(cnt):
    if cnt <= 0:
        return None
    for i in range(1, 10):
        bigNum2Str_r(str(i), cnt - 1)

def bigNum2Str_r(prefix, cnt):
    if cnt == 0:
        print(prefix)
        return
    for i in range(0, 10):
        bigNum2Str_r(prefix + str(i), cnt - 1)

if __name__ == '__main__':
    bigNum2Str(2)
    print
    bigNum2Str(3)
    print
