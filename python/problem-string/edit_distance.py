
def edit_distance(s1, s2):
    long = s1
    short = s2
    if len(s1) < len(s2):
        long = s2
        short = s1

    for l in range(len(short) - 1):
        if short[l:l+1] != long[l:l+1]:
            break
    print(l)
    r = -1
    while -len(short) < r:
        if short[r-1:r] != long[r-1:r]:
            break
        r -= 1
    print(r)
    print(short[l:len(short)+r], long[l:len(long)+r])

    return edit_distance_r(short[l:len(short)+r], long[l:len(long)+r])

def edit_distance_r(short, long):
    print('edit_distance_r', short, long)

    if short[:1] == long[:1]:
        return edit_distance_r(short[1:], long[1:])

    if len(short) == 1:
        if short[:1] in long:
            return len(long) - 1
        return len(long)
    return min(edit_distance_r(short[1:], long), edit_distance_r(short, long[1:])) + 1


#if __name__ == '__main__':
#    print(edit_distance('Saturday', 'Sunday'))


#   https://leetcode.com/problems/edit-distance

#   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346


class Solution:
    #   Wrong Answer
    def minDistance0(self, word1: str, word2: str) -> int:
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)
        i, cnt = 0, 0
        while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
            i += 1
            cnt += 1
        if 0 < cnt:
            word1, word2 = word1[i:], word2[i:]
        i, j, cnt = len(word1) - 1, len(word2) - 1, 0
        while 0 <= i and 0 <= j and word1[i] == word2[j]:
            i -= 1
            j -= 1
            cnt += 1
        if 0 < cnt:
            word1, word2 = word1[:i + 1], word2[:j + 1]
        def match(w1, w2):
            if 0 == len(w2) or 0 == len(w1) or len(set(w1).intersection(set(w2))) == 0:
                print('no match', w1, w2)
                return max(len(w1), len(w2))
            elif w2 in w1:
                print('w1 includes w2', w1, w2)
                return len(w1) - len(w2)
            elif w1 in w2:
                print('w2 includes w1', w1, w2)
                return len(w2) - len(w1)
            else:
                subRes = len(w1)
                for i, c in enumerate(w2):
                    if c not in w1:
                        continue
                    for idx in range(len(w1)):
                        if w1[idx] != c:
                            continue
                        subRes = min(subRes, match(w1[:idx], w2[:i]) + match(w1[idx + 1:], w2[i + 1:]))
                print(w1, w2)
                return subRes
        return match(word1, word2)

    #   Wrong Answer
    def minDistance1(self, word1: str, word2: str) -> int:
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)
        R, C = len(word2), len(word1)
        board = [[False] * C for _ in range(R)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if word1[c] == word2[r]:
                    board[r][c] = True
        matches = []
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if board[r][c] and (len(matches) == 0 or (matches[-1][0] > r and matches[-1][1] > c)):
                    matches.append((r, c))
        if 0 == len(matches):
            return max(len(word1), len(word2))
        cnt = max(R - 1 - matches[0][0], C - 1 - matches[0][1])
        for i, match in enumerate(matches):
            if 0 == i or (matches[i - 1][0] - match[0] == 1 and matches[i - 1][1] - match[1] == 1):
                continue
            cnt += max(matches[i - 1][0] - match[0], matches[i - 1][1] - match[1]) - 1
        cnt += max(matches[-1][0], matches[-1][1])
        return cnt

    #   Time Limit Exceeded
    def minDistance2(self, word1: str, word2: str) -> int:
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)
        R, C = len(word2), len(word1)
        self.cnt = max(R, C)

        def calcED(matches):
            cnt = max(matches[0][0], matches[0][1])
            for i, match in enumerate(matches):
                if 0 == i or (match[0] - matches[i - 1][0] == 1 and match[1] - matches[i - 1][1] == 1):
                    continue
                cnt += max(match[0] - matches[i - 1][0], match[1] - matches[i - 1][1]) - 1
            cnt += max(R - 1 - matches[-1][0], C - 1 - matches[-1][1])
            self.cnt = min(self.cnt, cnt)

        def getNextMatch(matches, minR, minC):
            if minR == R - 1 or minC == C - 1:
                calcED(matches)
            else:
                hasNoMoreMatch = True
                for r in range(minR + 1, R):
                    for c in range(minC + 1, C):
                        if word1[c] == word2[r]:
                            hasNoMoreMatch = False
                            matches.append((r, c))
                            getNextMatch(matches, r, c)
                            matches.pop()
                if hasNoMoreMatch:
                    calcED(matches)

        for r in range(R):
            for c in range(C):
                if word1[c] == word2[r]:
                    acc = [(r, c)]
                    getNextMatch(acc, r, c)
                    acc.pop()
        return self.cnt

    #   Time Limit Exceeded
    def minDistance3(self, word1: str, word2: str) -> int:
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)
        R, C = len(word2), len(word1)
        self.cnt = max(R, C)

        def getNextMatch(cnt, minR, minC):
            if self.cnt < cnt:
                return
            if minR == R - 1 or minC == C - 1:
                cnt += max(R - 1 - minR, C - 1 - minC)
                self.cnt = min(self.cnt, cnt)
            else:
                hasNoMoreMatch = True
                for r in range(minR + 1, R):
                    for c in range(minC + 1, C):
                        if word1[c] == word2[r]:
                            hasNoMoreMatch = False
                            if (r - minR == 1 and c - minC == 1):
                                getNextMatch(cnt, r, c)
                            else:
                                getNextMatch(cnt + max(r - minR, c - minC) - 1, r, c)
                if hasNoMoreMatch:
                    cnt += max(R - 1 - minR, C - 1 - minC)
                    self.cnt = min(self.cnt, cnt)

        for r in range(R):
            for c in range(C):
                if word1[c] == word2[r]:
                    getNextMatch(max(r, c), r, c)
        return self.cnt

    #   https://leetcode.com/problems/edit-distance/discuss/662395/Python-Classical-DP-O(mn)-explained
    #   runtime; 192ms, 60.64%
    #   memory; 17.4MB
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)
        R, C = len(word2), len(word1)
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(1, len(dp)):
            dp[r][0] = dp[r - 1][0] + 1
        for c in range(1, len(dp[0])):
            dp[0][c] = dp[0][c - 1] + 1
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                cost = 1 if word1[c - 1] != word2[r - 1] else 0
                dp[r][c] = min(dp[r - 1][c] + 1, dp[r][c - 1] + 1, dp[r - 1][c - 1] + cost)
        return dp[-1][-1]


s = Solution()
data = [('horse', 'ros', 3),
        ('intention', 'execution', 5),
        ('plasma', 'altruism', 6),
        ('a', 'b', 1),
        ('ab', 'b', 1),
        ('ab', 'c', 2),
        ('a', 'bc', 2),
        ('mart', 'karma', 3),
        ('pneumonoultramicroscopicsilicovolcanoconiosis', 'ultramicroscopically', 27),
        ]
for word1, word2, expect in data:
    real = s.minDistance(word1, word2)
    print(f'{word1} {word2} expect {expect} real {real} result {expect == real}')
