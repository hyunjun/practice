#   https://leetcode.com/problems/find-duplicate-file-in-system

#   https://leetcode.com/problems/find-duplicate-file-in-system/solution


class Solution:
    #   runtime; 144ms, 56.39%
    #   memory; 21.6MB, 100.00%
    def findDuplicate(self, paths):
        if paths is None or 0 == len(paths):
            return []
        d = {}
        for path in paths:
            data = path.split(' ')
            for i in range(1, len(data)):
                openIdx = data[i].index('(')
                filename, content = data[i][:openIdx], data[i][openIdx:]
                if content in d:
                    d[content].append('{}/{}'.format(data[0], filename))
                else:
                    d[content] = ['{}/{}'.format(data[0], filename)]
        print(d)
        return [l for l in d.values() if 1 < len(l)]


s = Solution()
data = [(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"], [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
        (["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"], []),
        ]
for paths, expected in data:
    real = s.findDuplicate(paths)
    print('{}, expected {}, real {}, result {}'.format(paths, expected, real, sorted(expected) == sorted(real)))
