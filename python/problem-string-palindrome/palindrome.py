import sys


def isPalindrome(num):
    if num is None:
        return False
    try:
        int(num)
    except ValueError:
        return False

    l, r = 0, len(num)
    while l <= r:
        if num[l:l+1] != num[r-1:r]:
            return False
        l += 1
        r -= 1
    return True


def isPalindrome2(num):
    if num is None:
        return False
    try:
        int(num)
    except ValueError:
        return False
    return num == num[::-1]


#    http://www.careercup.com/question?id=5177378863054848
def isPalindromeS(s):
    if s is None:
        return False
    if len(s) == 1:
        return True
    return s == s[::-1]


def numOfPalindrome(s):
    if s is None or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    result = 0
    if isPalindromeS(s):
        result += len(s)/2
        if len(s) % 2 == 1:
            result += 1
    else:
        return len(s)
    result += 2 * numOfPalindrome(s[:len(s) // 2])
    return result


if __name__ == '__main__':
    #input = sys.argv[1]
    #print(isPalindrome(input))
    #print(isPalindrome2(input))
    print(numOfPalindrome('aba'))
    print(numOfPalindrome('abc'))
    print(numOfPalindrome('abba'))
    print(numOfPalindrome('abcba'))
