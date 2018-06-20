import re

# http://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002216442

sentences = ['The history of apple computer', 'News for apple computer', 'The apple is the pomaceous fruit of the apple tree', 'apple computer is not the apple']

pattern_words = ['apple', 'apple (?!computer)', 'apple (?=computer)', '(?<=apple) computer']

for pattern_word in pattern_words:
  print('pattern: |{}|'.format(pattern_word))
  pattern = re.compile(pattern_word)
  for sentence in sentences:
    print('\t"{}" matched [{}]'.format(sentence, ','.join([m.group() for m in re.finditer(pattern, sentence)])))
