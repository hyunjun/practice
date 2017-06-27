import re


BLANK_PATTERN = re.compile('\s+')


def remove_blank_and_make_lower(s):
  return re.sub(BLANK_PATTERN, '', s).lower()
