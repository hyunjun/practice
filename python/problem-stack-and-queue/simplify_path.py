#   https://leetcode.com/problems/simplify-path


class Solution:
    #   runtime; 24ms, 95.62%
    #   memory; 13.8MB, 14.29%
    def simplifyPath(self, path: str) -> str:
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
