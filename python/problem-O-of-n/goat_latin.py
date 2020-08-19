#   https://leetcode.com/problems/goat-latin


class Solution:
    #   36ms; not have enough accepted submissions to show runtime distribution chart
    def toGoatLatin0(self, S):
        if S is None or 0 == len(S):
            return None
        result = []
        for i, word in enumerate(S.split()):
            if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result.append(word + 'ma' + 'a' * (i + 1))
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
        return ' '.join(result)

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429
    #   runtime; 32ms, 61.39%
    #   memory; 14.1MB
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i, w in enumerate(words):
            if not any(w.lower().startswith(v) for v in ['a', 'e', 'i', 'o', 'u']):
                w = w[1:] + w[0]
            words[i] = w + 'ma'
        return ' '.join(w + 'a' * (i + 1) for i, w in enumerate(words))


s = Solution()
data = [("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
        ("The quick brown fox jumped over the lazy dog", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"),
        ("Each word consists of lowercase and uppercase letters only", "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"),
        ]
for S, expected in data:
    real = s.toGoatLatin(S)
    print(f'{S} -> {expected}, result {expected == real}')
