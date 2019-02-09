#   https://py.checkio.org/mission/bird-language


VOWELS = "aeiouy"

def translate(phrase):
    i, ret = 0, []
    while i < len(phrase):
        c = phrase[i]
        ret.append(c)
        if c in VOWELS:
            i += 3
        elif ' ' == c:
            i += 1
        else:
            i += 2
    return ''.join(ret) 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
