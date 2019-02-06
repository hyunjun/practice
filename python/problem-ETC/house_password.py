#   https://py.checkio.org/mission/house-password/solve/

#   https://py.checkio.org/mission/house-password/publications/PositronicLlama/python-3/regular-expressions/?ordering=most_voted&filtering=choice


def checkio(data: str) -> bool:

    if data is None or len(data) < 10:
        return False
    hasNum, hasUpper, hasLower = False, False, False
    for d in data:
        if '0' <= d <= '9':
            hasNum = True
        elif 'A' <= d <= 'Z':
            hasUpper = True
        elif 'a' <= d <= 'z':
            hasLower = True
        if hasNum and hasUpper and hasLower:
            return True
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
