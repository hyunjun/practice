# Scrapy
* http://scrapy.org/
* http://doc.scrapy.org/en/latest/index.html
* https://github.com/scrapy/scrapy/wiki

## installation
* http://doc.scrapy.org/en/latest/intro/install.html

### prerequisite
* CentOS 6.3 기준
* cryptography
  * libffi-devel
    * situation; cryptography install failure
    ```
    pip install Scrapy; InstallationError: Command python setup.py egg_info failed with error code 1 in /tmp/pip_build_root/cryptography
    easy_install Scrapy; distutils.errors.DistutilsError: Setup script exited with error: command 'gcc' failed with exit status 1
    ```
    * cause; missing libffi-devel
    * solution
      * install libffi-devel from http://rpmfind.net/linux/rpm2html/search.php?query=libffi-devel
      * ftp://rpmfind.net/linux/centos/6.5/os/x86_64/Packages/libffi-devel-3.0.5-3.2.el6.x86_64.rpm
* lxml
  * libxml2-devel
    * situation; lxml install failure
    ```
    install lxml error: command 'gcc' failed with exit status 1
    ```
    * cause; missing libxslt-devel
    * solution; yum install libxslt-devel
  * libxslt-devel

## example
* wiki 정보가 구조화되어 있다면 Scrapy를 통해 더 간단하게 원하는 값을 얻을 수 있다
* 테스트; 송종국, 박지성의 국적 추출
* http://doc.scrapy.org/en/latest/topics/shell.html#topics-shell
* 송종국
```
$ scrapy shell http://ko.wikipedia.org/wiki/송종국
2014-05-13 09:05:58+0900 [scrapy] INFO: Scrapy 0.22.2 started (bot: scrapybot)
2014-05-13 09:05:58+0900 [scrapy] INFO: Optional features available: ssl, http11
2014-05-13 09:05:58+0900 [scrapy] INFO: Overridden settings: {'LOGSTATS_INTERVAL': 0}
2014-05-13 09:05:58+0900 [scrapy] INFO: Enabled extensions: TelnetConsole, CloseSpider, WebService, CoreStats, SpiderState
2014-05-13 09:05:58+0900 [scrapy] INFO: Enabled downloader middlewares: HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, HttpProxyMiddleware, ChunkedTransferMiddleware, DownloaderStats
2014-05-13 09:05:58+0900 [scrapy] INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
2014-05-13 09:05:58+0900 [scrapy] INFO: Enabled item pipelines:
2014-05-13 09:05:58+0900 [scrapy] DEBUG: Telnet console listening on 0.0.0.0:6024
2014-05-13 09:05:58+0900 [scrapy] DEBUG: Web service listening on 0.0.0.0:6081
2014-05-13 09:05:58+0900 [default] INFO: Spider opened
2014-05-13 09:05:58+0900 [default] DEBUG: Crawled (200) <GET http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD> (referer: None)
[s] Available Scrapy objects:
[s]   crawler    <scrapy.crawler.Crawler object at 0x2b81fd0>
[s]   item       {}
[s]   request    <GET http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD>
[s]   response   <200 http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD>
[s]   sel        <Selector xpath=None data=u'<html lang="ko" dir="ltr" class="client-'>
[s]   settings   <CrawlerSettings module=None>
[s]   spider     <Spider 'default' at 0x309b8d0>
[s] Useful shortcuts:
[s]   shelp()           Shell help (print this help)
[s]   fetch(req_or_url) Fetch request (or URL) and update local objects
[s]   view(response)    View response in a browser

>>> sel.xpath("//div[@id='content']/div[@id='bodyContent']/div[@id='mw-content-text']/table[1]/tr[5]/td[2]/span[1]/a[1]/text()[1]").extract()
[u'\ub300\ud55c\ubbfc\uad6d']
>>> print u'\ub300\ud55c\ubbfc\uad6d'
대한민국
>>> 
```
* 박지성
```
$ scrapy shell http://ko.wikipedia.org/wiki/박지성
2014-05-13 09:05:04+0900 [scrapy] INFO: Scrapy 0.22.2 started (bot: scrapybot)
2014-05-13 09:05:04+0900 [scrapy] INFO: Optional features available: ssl, http11
2014-05-13 09:05:04+0900 [scrapy] INFO: Overridden settings: {'LOGSTATS_INTERVAL': 0}
2014-05-13 09:05:04+0900 [scrapy] INFO: Enabled extensions: TelnetConsole, CloseSpider, WebService, CoreStats, SpiderState
2014-05-13 09:05:04+0900 [scrapy] INFO: Enabled downloader middlewares: HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, HttpProxyMiddleware, ChunkedTransferMiddleware, DownloaderStats
2014-05-13 09:05:04+0900 [scrapy] INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
2014-05-13 09:05:04+0900 [scrapy] INFO: Enabled item pipelines:
2014-05-13 09:05:04+0900 [scrapy] DEBUG: Telnet console listening on 0.0.0.0:6023
2014-05-13 09:05:04+0900 [scrapy] DEBUG: Web service listening on 0.0.0.0:6080
2014-05-13 09:05:04+0900 [default] INFO: Spider opened
2014-05-13 09:05:04+0900 [default] DEBUG: Crawled (200) <GET http://ko.wikipedia.org/wiki/%EB%B0%95%EC%A7%80%EC%84%B1> (referer: None)
[s] Available Scrapy objects:
[s]   crawler    <scrapy.crawler.Crawler object at 0x31fcfd0>
[s]   item       {}
[s]   request    <GET http://ko.wikipedia.org/wiki/%EB%B0%95%EC%A7%80%EC%84%B1>
[s]   response   <200 http://ko.wikipedia.org/wiki/%EB%B0%95%EC%A7%80%EC%84%B1>
[s]   sel        <Selector xpath=None data=u'<html lang="ko" dir="ltr" class="client-'>
[s]   settings   <CrawlerSettings module=None>
[s]   spider     <Spider 'default' at 0x37168d0>
[s] Useful shortcuts:
[s]   shelp()           Shell help (print this help)
[s]   fetch(req_or_url) Fetch request (or URL) and update local objects
[s]   view(response)    View response in a browser

>>> sel.xpath("//div[@id='content']/div[@id='bodyContent']/div[@id='mw-content-text']/table[1]/tr[4]/td[2]/span[1]/a[1]/text()[1]").extract()
[u'\ub300\ud55c\ubbfc\uad6d']
>>> print u'\ub300\ud55c\ubbfc\uad6d'
대한민국
>>>
```
* http://doc.scrapy.org/en/latest/intro/overview.html#intro-overview-item
```
$ scrapy startproject song
$ cd song/
$ tree .
.
├── scrapy.cfg
└── song
  ├── __init__.py
  ├── items.py
  ├── pipelines.py
  ├── settings.py
  └── spiders
  └── __init__.py

2 directories, 6 files
$ vi song/items.py song/spiders/SongSpider.py
2 files to edit
$ cat song/items.py song/spiders/SongSpider.py

#-*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SongItem(Item):
  url = Field()
  nationality = Field()

#-*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from song.items import SongItem

class SongSpider(CrawlSpider):

  name = 'song'
  allowed_domains = ['wikipedia.org']
  start_urls = ['http://ko.wikipedia.org/wiki/송종국']
  #start_urls = ['http://ko.wikipedia.org/wiki/송종국', 'http://ko.wikipedia.org/wiki/박지성']
  #start_urls = ['http://ko.wikipedia.org/wiki/']
  #rules = [Rule(SgmlLinkExtractor(allow=['//송종국']), 'parse')]
  #rules = [Rule(SgmlLinkExtractor(allow=['/%EC%86%A1%EC%A2%85%EA%B5%AD']), 'parse')]

  def parse(self, response):
    sel = Selector(response)
    songItem = SongItem()
    songItem['url'] = response.url
    songItem['nationality'] = sel.xpath("//div[@id='content']/div[@id='bodyContent']/div[@id='mw-content-text']/table[1]/tr[5]/td[2]/span[1]/a[1]/text()[1]").extract()[0]
    open('test.song', 'wb').write(response.body)
    open('test.song', 'wb').write(songItem['nationality'])
    print songItem['url']
    print songItem['nationality'], type(songItem['nationality'])
    return songItem

$ scrapy crawl song -o song.json -t json
2014-05-13 09:19:22+0900 [scrapy] INFO: Scrapy 0.22.2 started (bot: song)
2014-05-13 09:19:22+0900 [scrapy] INFO: Optional features available: ssl, http11
2014-05-13 09:19:22+0900 [scrapy] INFO: Overridden settings: {'NEWSPIDER_MODULE': 'song.spiders', 'FEED_FORMAT': 'json', 'SPIDER_MODULES': ['song.spiders'], 'FEED_URI': 'song.json', 'BOT_NAME': 'song'}
2014-05-13 09:19:22+0900 [scrapy] INFO: Enabled extensions: FeedExporter, LogStats, TelnetConsole, CloseSpider, WebService, CoreStats, SpiderState
2014-05-13 09:19:22+0900 [scrapy] INFO: Enabled downloader middlewares: HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, HttpProxyMiddleware, ChunkedTransferMiddleware, DownloaderStats
2014-05-13 09:19:22+0900 [scrapy] INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
2014-05-13 09:19:22+0900 [scrapy] INFO: Enabled item pipelines:
2014-05-13 09:19:22+0900 [song] INFO: Spider opened
2014-05-13 09:19:22+0900 [song] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2014-05-13 09:19:22+0900 [scrapy] DEBUG: Telnet console listening on 0.0.0.0:6023
2014-05-13 09:19:22+0900 [scrapy] DEBUG: Web service listening on 0.0.0.0:6080
2014-05-13 09:19:23+0900 [song] DEBUG: Crawled (200) <GET http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD> (referer: None)
http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD
대한민국 <type 'unicode'>
2014-05-13 09:19:23+0900 [song] DEBUG: Scraped from <200 http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD>
    {'nationality': u'\ub300\ud55c\ubbfc\uad6d',
     'url': 'http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD'}
2014-05-13 09:19:23+0900 [song] INFO: Closing spider (finished)
2014-05-13 09:19:23+0900 [song] INFO: Stored json feed (1 items) in: song.json
2014-05-13 09:19:23+0900 [song] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 247,
     'downloader/request_count': 1,
     'downloader/request_method_count/GET': 1,
     'downloader/response_bytes': 28294,
     'downloader/response_count': 1,
     'downloader/response_status_count/200': 1,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2014, 5, 13, 0, 19, 23, 257728),
     'item_scraped_count': 1,
     'log_count/DEBUG': 4,
     'log_count/INFO': 8,
     'response_received_count': 1,
     'scheduler/dequeued': 1,
     'scheduler/dequeued/memory': 1,
     'scheduler/enqueued': 1,
     'scheduler/enqueued/memory': 1,
     'start_time': datetime.datetime(2014, 5, 13, 0, 19, 22, 673319)}
2014-05-13 09:19:23+0900 [song] INFO: Spider closed (finished)
$ cat song.json
[{"url": "http://ko.wikipedia.org/wiki/%EC%86%A1%EC%A2%85%EA%B5%AD", "nationality": "\ub300\ud55c\ubbfc\uad6d"}]
```
