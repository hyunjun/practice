#   https://leetcode.com/problems/rearrange-words-in-a-sentence


class Solution:
    #   runtime; 88ms, 16.67%
    #   memory; 17.5MB, 100.00%
    def arrangeWords(self, text: str) -> str:
        if text is None or not (1 <= len(text) <= 10 ** 5):
            return text
        l = [(word.lower(), len(word), i) for i, word in enumerate(text.split(' '))]
        return ' '.join(w for w, _, _ in sorted(l, key=lambda t: (t[1], t[2]))).capitalize()


s = Solution()
data = [("Leetcode is cool", "Is cool leetcode"),
        ("Keep calm and code on", "On and keep calm code"),
        ("To be or not to be", "To be or to be not"),
        ]
for text, expected in data:
    real = s.arrangeWords(text)
    print(f'{text} expected {expected} real {real} result {expected == real}')
