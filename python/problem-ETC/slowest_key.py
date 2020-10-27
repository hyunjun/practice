#   https://leetcode.com/problems/slowest-key


from typing import List


class Solution:
    #   runtime; 232 ms, 7.03%
    #   memory; 14.5 MB, 6.39%
    def slowestKey0(self, releaseTimes: List[int], keysPressed: str) -> str:
        diffs = [t if i == 0 else t - releaseTimes[i - 1] for i, t in enumerate(releaseTimes)]
        return sorted([k for k, d in zip(keysPressed, diffs) if d == max(diffs)])[-1]

    #   runtime; 48 ms, 99.43%
    #   memory; 14.5 MB, 6.39%
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxReleaseTime, keyPressed = releaseTimes[0], keysPressed[0]
        for i, t in enumerate(releaseTimes):
            if i == 0:
                continue
            curReleaseTime = t - releaseTimes[i - 1]
            if maxReleaseTime < curReleaseTime:
                maxReleaseTime, keyPressed = curReleaseTime, keysPressed[i]
            elif curReleaseTime == maxReleaseTime and keyPressed < keysPressed[i]:
                keyPressed = keysPressed[i]
        return keyPressed


s = Solution()
data = [([9,29,49,50], "cbcd", "c"),
        ([12,23,36,46,62], "spuda", "a"),
        ]
for releaseTimes, keysPressed, expect in data:
    real = s.slowestKey(releaseTimes, keysPressed)
    print(f'{releaseTimes} {keysPressed} expect {expect} real {real} result {expect == real}')
