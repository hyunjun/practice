
inp = raw_input()
i, start, quotation_open = 0, 0, False

while i < len(inp):
  if quotation_open == False and inp[i] in ['.', '!', '?']:
    print inp[start:i + 1].strip()
    start = i + 1
  elif inp[i] in ['"']:
    quotation_open = not quotation_open
  i += 1
