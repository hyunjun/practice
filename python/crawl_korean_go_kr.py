# -*- coding: utf8 -*-
import requests
import bs4

'''
http://www.slideshare.net/changwonchoe7/141118-41835245
https://github.com/kennethreitz/requests/issues/2875
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

외래어 표기법 용례 찾기
http://www.korean.go.kr/front/foreignSpell/foreignSpellList.do?mn_id=96
http://www.korean.go.kr/front/foreignSpell/foreignSpellList.do?mn_id=96&pageIndex=5823
국어의 로마자 표기법
http://www.korean.go.kr/front/roman/romanList.do?mn_id=98
http://www.korean.go.kr/front/roman/romanList.do?mn_id=98&pageIndex=1231
다듬은 말(순화어)
http://www.korean.go.kr/front/refine/refineList.do?mn_id=34
http://www.korean.go.kr/front/refine/refineList.do?mn_id=34&pageIndex=2144
'''

if __name__ == '__main__':
  urls = ['http://www.korean.go.kr/front/foreignSpell/foreignSpellList.do?mn_id=96&pageIndex=5823',
          'http://www.korean.go.kr/front/roman/romanList.do?mn_id=98&pageIndex=1231',
          'http://www.korean.go.kr/front/refine/refineList.do?mn_id=34&pageIndex=2144']
  for url in urls:
    response = requests.get(url)
    html_content = response.text.encode(response.encoding)
    parsed_html = bs4.BeautifulSoup(html_content, 'html.parser')
    for i in parsed_html.tbody.find_all('td'):
      print i.string
