#   similar version in scala; https://gist.github.com/hyunjun/ccf149468a9d87857d0ce673e0127eb1


def permutation(acc, prev, cur):
    if 0 == len(cur):
        return [prev]
    else:
        result = []
        [result.extend(permutation(acc, prev + cur[i], cur[:i] + cur[i + 1:])) for i in range(0, len(cur))]
        return result


acc = []
acc.extend(permutation(acc, "", "aet"))
print(acc)


acc = []
acc.extend(permutation(acc, "", "aaet"))
print(acc)
