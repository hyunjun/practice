#   https://leetcode.com/problems/goat-latin
#   36ms; not have enough accepted submissions to show runtime distribution chart


class Solution:
    def toGoatLatin(self, S):
        if S is None or 0 == len(S):
            return None
        result = []
        for i, word in enumerate(S.split()):
            if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result.append(word + 'ma' + 'a' * (i + 1))
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
        return ' '.join(result)


s = Solution()
data = [
    ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
    ("The quick brown fox jumped over the lazy dog", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"),
    ("Each word consists of lowercase and uppercase letters only", "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa")
    ]
for inp, expected in data:
    real = s.toGoatLatin(inp)
    print('{} -> {}, result {}'.format(inp, real, expected == real))
