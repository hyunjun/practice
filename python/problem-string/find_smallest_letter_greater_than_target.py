#   https://leetcode.com/problems/find-smallest-letter-greater-than-target

#   https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution


class Solution:
    #   Wrong Answer
    def nextGreatestLetter0(self, letters, target):
        if target < letters[0]:
            return letters[0]
        elif letters[-1] <= target:
            return letters[0]
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l + r) // 2
            if target <= letters[m]:
                if m + 1 < len(letters) and target < letters[m + 1]:
                    return letters[m + 1]
                if target == letters[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l = m + 1
        return -1

    #   10.00%
    def nextGreatestLetter(self, letters, target):
        uniqueLetters = [letters[0]]
        counts = [1]
        for i, letter in enumerate(letters):
            if 0 == i:
                continue
            if letters[i - 1] == letter:
                counts[-1] += 1
            else:
                uniqueLetters.append(letter)
                counts.append(1)
        if target < uniqueLetters[0] or uniqueLetters[-1] <= target:
            return uniqueLetters[0]
        for i in range(len(uniqueLetters) - 1):
            if uniqueLetters[i] <= target < uniqueLetters[i + 1]:
                return uniqueLetters[i + 1]
        return -1


s = Solution()
data = [(['c', 'f', 'j'], 'a', 'c'),
        (['c', 'f', 'j'], 'c', 'f'),
        (['c', 'f', 'j'], 'd', 'f'),
        (['c', 'f', 'j'], 'g', 'j'),
        (['c', 'f', 'j'], 'j', 'c'),
        (['c', 'f', 'j'], 'k', 'c'),
        ]
for letters, target, expected in data:
    real = s.nextGreatestLetter(letters, target)
    print('{}, {}, expected {}, real {}, result {}'.format(letters, target, expected, real, expected == real))
