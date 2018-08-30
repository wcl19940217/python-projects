import requests
from bs4 import BeautifulSoup
import datetime
import simplejson

start = datetime.datetime.now()
url = 'http://www.mafengwo.cn/wenda/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

soup = BeautifulSoup(requests.get(url=url, headers=header).text.encode('utf-8'), 'lxml')
s = soup.select('div[class="avatar"] a')
s1 = soup.select('div[class="title"] a')
# print(s1)
# 可以直接用的url
urls = []
# 需要再次处理的
urls_two = []
ua = 'http://www.mafengwo.cn'
for i in s:
    ur = i["href"]
    # print(ur)
    # urls.append(ua + ur)

for i in s1:
    ur = i["href"]
    # urls_two.append(ua + ur)
# print(urls_two)

for i in range(11, 21):
    url = 'http://www.mafengwo.cn/qa/ajax_qa/more?type=1&mddid=&tid=&sort=8&key=&page={}&time='.format(i)

    r1 = requests.get(url=url, headers=header)
    s = simplejson.loads(r1.content)
    for k, v in s.items():
        d = v['html']
        soup = BeautifulSoup(d.encode('utf-8'), 'lxml')
        s = soup.select('div[class="avatar"] a')
        s1 = soup.select('div[class="title"] a')
        for i in s:
            ur = i["href"]
            urls.append(ua + ur)
        print(1, urls)

        for i in s1:
            ur = i["href"]
            urls_two.append(ua + ur)
        print(2, urls_two)

for urls2 in urls_two:
    soup = BeautifulSoup(requests.get(url=urls2, headers=header).text.encode('utf-8'), 'lxml')
    s = soup.select('a[class="name"] ')
    # s1 = soup.select('ul[class="comment-list _j_comment_list_ul"] a ')
    # s2 = soup.select('li[class="comment-item clearfix"] a ')
    s3 = soup.select('div[class="comment-user"] a ')
    # #print(s3)
    #
    # try:
    #     for i in s3:
    #         ur = i["href"]
    #         ua = 'http://www.mafengwo.cn/wenda'
    #         urls.append(ua + ur)
    #     print(1,len(urls))
    # except Exception as e:
    #     print(e)

    # print()
    try:
        for i in s:
            ur = i["href"]
            urls.append(ua + ur)
        print(2, len(urls))

    except Exception as e:
        print(e)
    with open('c:/assets/urls', 'a+', encoding='utf-8') as f1:
        f1.write(str(urls))
        f1.flush()

l = []
l1 = []
l2 = []
l3 = []
d = {}
l8 = []
l9 = []
for url1 in urls:
    soup = BeautifulSoup(requests.get(url=url1, headers=header).text.encode('utf-8'), 'lxml')
    s = soup.select('div[class="MAvaName"]')
    s1 = soup.select('span[class="MAvaLevel flt1"] a')
    s2 = soup.select('div [class="MAvaMore clearfix"] a')
    s3 = soup.select('div[class="achievement clearfix"] strong')

    # 昵称
    for i in s:
        l.append(i.text.strip())

        # 等级
    for i in s1:
        l1.append(i.text)

    for i in s2:
        l2.append(i.text)

    # #回答三个数据
    for i in s3:
        l3.append(i.text)

# 改成嵌套列表
for j in range(0, len(l2), 3):
    l8.append([l2[j], l2[j + 1], l2[j + 2]])
# print(l8)

for i in range(0, len(l3), 3):
    l9.append([l3[i], l3[i + 1], l3[i + 2]])
# print(l9)

# 每个元素全部追加到嵌套列表中。
for i in range(len(l)):
    d[i] = [{'name': '{}'.format(l[i])}]

for i in range(len(l1)):
    d[i].append({'level': '{}'.format(l1[i])})

for i in range(len(l8)):
    d[i].append({'关注，粉丝、蜂蜜': '{}'.format(l8[i])})

for j in range(len(l9)):
    d[j].append({'回答数，金牌回答，采纳率': '{}'.format(l9[j])})
# print(d,end='\n')

with open('c:/assets/mafengwo', 'a+', encoding='utf-8') as f:
    for k, v in d.items():
        f.write('{}{}\n'.format(k, v))
        f.flush()

# import csv
# from pathlib import Path
#
# p = Path('c:/assets/wenda.csv')
# parent = p.parent
# if not parent.exists():
#     parent.makdir(parents =True)
#
# # with open(str(p),'a+')as f:
# #     reader = csv.reader(f)
# #     print(next(reader))
# #     print(next(reader))
#
# rows = [
# [l[i] for i in range(len(l))],
#     [l1[i] for i in range(len(l1))],
#     [l8[i] for i in range(len(l8))],
#     [l9[i] for i in range(len(l9))]
# ]
# # row =rows[0]
#
# with open(str(p),'w+')as f:
#     writer = csv.writer(f)
#     # writer.writerow(row)
#     writer.writerows(rows)

delta = (datetime.datetime.now() - start)
print(delta.total_seconds())
