#   https://py.checkio.org/mission/most-wanted-letter


def checkio(text: str) -> str:

    d = {}
    for c in text.lower():
        if 'a' <= c <= 'z':
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    maxCnt, maxCntChar = 0, None
    for i in range(ord('a'), ord('z') + 1):
        c = chr(i)
        if c in d and maxCnt < d[c]:
            maxCnt, maxCntChar = d[c], c
    # sorted(d.items(), key=lambda t: (-t[1], ord(t[0])))
    # max('abcdefghijklmnopqrstuvwxyz', key=text.lower().count)
    return maxCntChar

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
