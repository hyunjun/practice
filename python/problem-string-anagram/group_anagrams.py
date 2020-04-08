# https://leetcode.com/problems/group-anagrams


class Solution(object):
    # 36.43%
    def groupAnagrams0(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or 0 == len(strs):
            return []
        result_dict, index_dict = {}, {}
        for i, s in enumerate(strs):
            key = ''.join(sorted(s))
            if key in result_dict:
                result_dict[key].append(s)
            else:
                result_dict[key] = [s]
                index_dict[key] = i
        result = []
        for key, i in sorted(index_dict.items(), key=lambda t: t[1]):
            result.append(sorted(result_dict[key]))
        return result

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288
    #   runtime; 104ms, 72.60%
    #   memory; 16.8MB
    def groupAnagrams(self, strs):
        if strs is None or 0 == len(strs):
            return [[]]
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())


cases = [(["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat","tea"], ["nat","tan"], ["bat"]])]
s = Solution()
for strs, expected in cases:
    real = s.groupAnagrams(strs)
    print(f'{strs} expected {expected} real {real} result {[sorted(e) for e in expected] == [sorted(r) for r in real]}')
