#   https://leetcode.com/problems/simplify-path


class Solution:
    #   runtime; 24ms, 95.62%
    #   memory; 13.8MB, 14.29%
    def simplifyPath0(self, path: str) -> str:
        if path is None or 0 == len(path):
            return ''

        while '//' in path:
            path = path.replace('//', '/')
        if path[-1] == '/':
            path = path[:-1]
        stack, dirs = [], path.split('/')
        for d in dirs:
            if '' == d or '.' == d:
                continue
            if '..' == d:
                if 0 < len(stack):
                    stack.pop()
            else:
                stack.append(d)
        ret = '/'.join(stack)
        return '/' + ret

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629
    #   runtime; 28ms, 89.96%
    #   memory; 14.2MB, 76.40%
    def simplifyPath(self, path: str) -> str:
        if path is None or 0 == len(path):
            return path

        stack = []
        for n in path.split('/'):
            if 0 == len(n) or '.' == n:
                continue
            if '..' == n:
                if 0 < len(stack):
                    stack.pop()
            else:
                stack.append(n)
        return '/' + '/'.join(stack)


s = Solution()
data = [("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/a/../../b/../c//.//", "/c"),
        ("/a//b////c/d//././/..", "/a/b/c"),
        ]
for path, expected in data:
    real = s.simplifyPath(path)
    print(f'{path} expected {expected} real {real} result {expected == real}')
