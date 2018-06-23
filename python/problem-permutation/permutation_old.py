
def print_permutation(s):
    if s is None or len(s) == 0:
            return
    print_permutation_r('', s)


def print_permutation_r(prefix, s):
    if len(s) == 1:
        print(prefix + s)
    for i in range(len(s)):
        #print(prefix + s[i:i+1], s[:i] + s[i+1:])
        print_permutation_r(prefix + s[i:i+1], s[:i] + s[i+1:])


if __name__ == '__main__':
    print_permutation(None)
    print_permutation('')
    print_permutation('a')
    print_permutation('ab')
    print_permutation('abc')
