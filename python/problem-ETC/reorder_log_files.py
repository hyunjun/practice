#   https://leetcode.com/problems/reorder-log-files


class Solution:
    #   52ms, 100.00%
    def reorderLogFiles(self, logs):
        def isLetterLogs(log):
            if '0' <= log[-1] <= '9':
                return False
            return True

        letterLogs, digitLogs = [], []
        for log in logs:
            if isLetterLogs(log):
                letterLogs.append(log)
            else:
                digitLogs.append(log)

        return sorted(letterLogs, key=lambda t: ' '.join(t.split(' ')[1:])) + digitLogs


s = Solution()
data = [(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"], ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]),
        ]
for logs, expected in data:
    real = s.reorderLogFiles(logs)
    print('{}, expected {}, real {}, result {}'.format(logs, expected, real, expected == real))
