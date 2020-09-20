#   https://leetcode.com/problems/rearrange-spaces-between-words


class Solution:
    #   runtime; 28ms, 60.00%
    #   memory; 13.8MB, 60.00%
    def reorderSpaces(self, text: str) -> str:
        cnt, texts = text.count(' '), text.split()
        if cnt == 0 and len(texts) <= 1:
            return text
        unit, extra = cnt // (len(texts) - 1) if len(texts) != 1 else 0, cnt % (len(texts) - 1) if len(texts) != 1 else cnt
        texts[-1] = f"{texts[-1]}{' ' * extra}"
        return (' ' * unit).join(texts)


s = Solution()
data = [("  this   is  a sentence ", "this   is   a   sentence"),
        (" practice   makes   perfect", "practice   makes   perfect "),
        ("hello   world", "hello   world"),
        ("  walks  udp package   into  bar a", "walks  udp  package  into  bar  a "),
        ("a", "a"),
        ("  hello", "hello  "),
        ]
for text, expect in data:
    real = s.reorderSpaces(text)
    print(f'{text}\n\texpect\t|{expect}|\n\treal\t|{real}|\n\tresult {expect == real}')
