#   https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent


from typing import List


class Solution:

    #   Wrong
    def arrayStringsAreEqual0(self, word1: List[str], word2: List[str]) -> bool:
        if word1 is None or 0 == len(word2) or word2 is None or 0 == len(word2):
            return False
        word1.sort()
        word2.sort()
        return ''.join(word1) == ''.join(word2)

    #   Time Limit Exceeded
    def arrayStringsAreEqual1(self, word1: List[str], word2: List[str]) -> bool:
        if word1 is None or 0 == len(word2) or word2 is None or 0 == len(word2) or len(''.join(word1)) != len(''.join(word2)):
            return False

        def joinStr(wordSet, acc, words):
            if 0 == len(words):
                wordSet.add(''.join(acc))
            else:
                for i, word in enumerate(words):
                    acc.append(word)
                    joinStr(wordSet, acc, words[:i] + words[i + 1:])
                    acc.pop()

        s1, s2 = set(), set()
        joinStr(s1, [], word1)
        joinStr(s2, [], word2)
        return 0 < len(s1.intersection(s2))

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597
    #   runtime; 40ms, 19.73%
    #   memory; 14.3MB, 63.95%
    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        if word1 is None or 0 == len(word2) or word2 is None or 0 == len(word2) or len(''.join(word1)) != len(''.join(word2)):
            return False
        return ''.join(word1) == ''.join(word2)

    #   https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/discuss/1007290/Python-Faster-and-less-memory-O(min(n-m))-and-O(1)-vs-O(n%2Bm)-and-O(n%2Bm)
    #   runtime; 64ms
    #   memory; 14.2MB, 63.95%
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.gen(word1), self.gen(word2)):
            if c1 != c2:
                return False
        return True

    def gen(self, word: List[str]):
        for s in word:
            for c in s:
                yield c
        # Ensure False when len(word1) != len(word2)
        yield None


s = Solution()
data = [(["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True),
        (["jbboxe","yshcrtanrtlzyyp","vudsssnzuef","lde"], ["jbboxeyshcrtanrt","lzyypvudsssnzueflde"], True),
        (["petiiycdncfxzhmefdrwjnprxbwxxaqqcbnsquupraxcgbbhpd","bbhiugowzemkgcuajtfyxulmwqyreuffmufakhvqsxhwqbmhubz","duuqyzvv","uuaqtztoojk","p","ppootkhdvkodfcscjkd","zqrvcnnjpelcdpqdbhhfjrkejxjlhqtqtexospsieyojkvlsdoapvbemubbxsctiawbzuyphnjvtrudfptiqv","xt","j","s","b"], ["petiiycdncfxzhmefdrwjnprxbwxxaqqcbnsquupraxcgbbhpdbbhiugowzemkgcuajtfyxulmwqyreuffmufakhvqsxhwqbmhubzdu","ojkpppootkhdvkodfcscjkdzqrvcnnjpelcdpqdbhhfjrkejxjl","hqtqtexospsieyojk","vlsdoapvbemubbxsctiawbzuyphnjvtrudfptiqvxtj","s","b","trizjjrzgyfhra"], False),
        (["tjup","mtpkkhgocld","rzpmmscccgzpqkadecsmypqt","lk","ek","vqenr","j"], ["tjupmtpkkhgocldr","zpmmscccgzpqkadecsmy","pqtlkekvqenrj"], True),
        ]
for word1, word2, expect in data:
    real = s.arrayStringsAreEqual(word1, word2)
    print(f'{word1} {word2} expect {expect} real {real} result {expect == real}')
