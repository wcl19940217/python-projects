import urllib3
from urllib.parse import urlencode
from urllib3 import HTTPResponse
import requests
from lxml import etree

# url = 'http://movie.douban.com'

ua =  'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

jurl = 'https://movie.douban.com/j/search_subjects'

d = {
    'type':'movie',
    'tag':'热门',
    'page_limit':10,
    'page_start':10
}
# urls = ['https://www.baidu.com/s?wd=magedu','https://www.baidu.com/s?wd=magedu']
urls = ['https://movie.douban.com/']

session = requests.Session()
with session:
    for url in urls:
        response = session.get(url,headers={'User-agent':ua})
        with response:
            content = response.text

        html = etree.HTML(content)
        print(html)
        title = html.xpath("//div[@class='billboard-bd']//tr")
        for t in title:
            txt = t.xpath('.//text()')
            print(''.join(map(lambda x:x.strip(),txt)))
            # print(t)