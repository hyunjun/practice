if __name__ == '__main__':
  N = int(raw_input())
  for i in range(N):
    keyword, cipher = raw_input(), raw_input()
    # print keyword
    keywords = []
    for j in range(len(keyword)):
      if keyword[j] not in keywords:
        keywords.append(keyword[j])
    # print keywords
    codes, rows = [], []
    codes.append(keywords)
    for j in range(65, 91):
      if 0 < len(rows) and len(rows) % len(keywords) == 0:
        codes.append(rows)
        rows = []
      if chr(j) not in keywords:
        rows.append(chr(j))
    codes.append(rows)
    # print codes
    orders = []
    for c in sorted(keywords):
      orders.append(''.join(keywords).index(c))
    # print orders
    code = []
    for j in orders:
      for row in codes:
        if j < len(row):
          code.append(row[j])
    # print code
    code_dict = {code[idx - 65]:chr(idx) for idx in range(65, 91)}
    code_dict[' '] = ' '
    print ''.join([code_dict[c] for c in cipher])
