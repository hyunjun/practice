import re
import sys

p = re.compile('[.\n]+')
trigrams, lines = {}, [line for line in sys.stdin]
words = re.sub(p, ' ', ' '.join(lines).lower()).split()

for i in range(len(words)):
  if i + 2 < len(words):
    trigram = ' '.join(words[i:i + 3]).strip()
    if trigram in trigrams:
      trigrams[trigram] += 1
    else:
      trigrams[trigram] = 1

max_key, max_cnt = None, 0
for trigram, cnt in trigrams.items():
  if cnt > max_cnt:
    max_key, max_cnt = trigram, cnt

print max_key
