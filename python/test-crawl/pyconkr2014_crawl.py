from __future__ import unicode_literals
from gevent import monkey; monkey.patch_all() # pip install greenlet; http://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent for win64bit
from gevent.pool import Pool
from scrapy.selector import Selector  # pip install Scrapy
from urlparse import urljoin

import requests # pip install requests


# pyconkr 2014  http://www.youtube.com/watch?v=TcORgdlJFM8

def fetch_page(url):
  '''1. 웹페이지 다운로드'''
  r = requests.get(url)
  return r.text


def talk_links_from_listpage(url):
  '''2. 목록 페이지에서 강의 링크 추출'''
  html = fetch_page(url)
  sel = Selector(text=html)
  talk_links = sel.css('.talk-link .media__message a::attr(href)').extract()
  talk_links = [urljoin(url, talk_link) for talk_link in talk_links]
  return talk_links


def talk_from_page(url):
  '''3. 강의 페이지에서 강의 메타정보 추출'''
  html = fetch_page(url)
  sel = Selector(text=html)
  title = sel.css('.talk-hero__title::text').extract()
  description = sel.css('.talk-description::text').extract()
  return {
    'title': title,
    'description': description
  }



def latest_talks(page=1):
  '''4. 최근 강의 목록 반환'''
  list_url = 'http://www.ted.com/talks/browse?page={0}'.format(page)
  talk_links = talk_links_from_listpage(list_url)
  # talks = [talk_from_page(url) for url in talk_links]
  pool = Pool(20)
  talks = pool.map(talk_from_page, talk_links)
  return talks


url = 'http://www.ted.com/talks/browse'

# with open('sample.html', 'w') as f:
#  f.write(fetch_page(url).encode('utf8'))

#from pprint import pprint
#pprint(talk_links_from_listpage(url))

#print talk_from_page('http://www.ted.com/talks/jorge_soto_the_future_of_early_cancer_detection')

from pprint import pprint
pprint(latest_talks())
