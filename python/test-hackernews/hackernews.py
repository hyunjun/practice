# -*- coding: utf8 -*-
import json
import re
import urllib


NUM_PATTERN = re.compile('\d+')
# https://github.com/HackerNews/API
MAX_ITEM_URL = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
TOPSTORIES_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
NEWSTORIES_URL = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
# https://wiki.python.org/moin/RssLibraries


def item_url(number):
  return 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(number)


if __name__ == '__main__':
  max_num = int(urllib.urlopen(MAX_ITEM_URL).read())
  print max_num
  item_num_string = ''.join([urllib.urlopen(url).read() for url in [TOPSTORIES_URL, NEWSTORIES_URL]])
  print item_num_string
  item_nums = set([item_num.group() for item_num in re.finditer(NUM_PATTERN, item_num_string)])
  item_urls = [item_url(item_num) for item_num in item_nums]
  print item_urls
  dicts = []
  for url in item_urls:
    print url
    d = json.loads(urllib.urlopen(url).read())
    title, url = d['title'], d['url']
    if title is None or url is None or 0 == len(title) or 0 == len(url):
      continue
    print d['id'], d['score']
    dicts.append(d)

  with open('result.md', 'w') as f:
    for d in sorted(dicts, key=lambda d: d['score'], reverse=True):
      title, url = d['title'], d['url']
      try:
        f.write('* [{}]({})\n'.format(title, url))
      except UnicodeEncodeError:
        f.write('* [{}]({})\n'.format(title.encode('utf8'), url.encode('utf8')))
