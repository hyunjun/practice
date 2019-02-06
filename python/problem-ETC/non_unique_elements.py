#   https://py.checkio.org/mission/non-unique-elements


def checkio(data: list) -> list:
    cntDict = {}
    for num in data:
        if num in cntDict:
            cntDict[num] += 1
        else:
            cntDict[num] = 1
    for num, cnt in cntDict.items():
        if 1 < cnt:
            continue
        data.remove(num)
    return data


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

