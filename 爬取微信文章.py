#__author: Joey
#date:    2018/5/18

import urllib.request
import re
import urllib.error
import time
import os
def use_proxy(proxy_addr,url):
    try:
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})

        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 创建一个opener对象
        opener.addheader = [headers]

        urllib.request.install_opener(opener)  # 安装该opener对象到全局

        data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        time.sleep(5)
    except Exception as e:
        print('exception:',str(e))
        time.sleep(1)

key = urllib.request.quote('python')
page_num = 1
url = 'http://weixin.sogou.com/weixin?query='+key+'&_sug_type_=&sut=1947&lkt=1%2C1526644073998%2C1526644073998&s_from=input&_sug_=y&type=2&sst0=1526644074099&page='+str(page_num)+'&ie=utf8&w=01019900&dr=1'

page = use_proxy('127.0.0.1:8888',url)

pattern_article = re.compile(r'<div class="txt-box">.*?href="(.*?)"',re.S)
pattern_title = re.compile(r'id="activity-name">(.*?)</h2>',re.S)
articles = re.findall(pattern_article,page)
for i in range(0,len(articles)):
    article_url = articles[i].replace('amp;','')
    article = use_proxy('127.0.0.1:8888',article_url)
    title = re.findall(pattern_title,article)[0].strip()
    title = title.replace(' ','')
    file = os.path.join(os.path.abspath('.'),title+'.html')
    try:
        with open(file,'w',encoding='utf-8') as f:    #open file 默认编码是gbk
            f.write(article)
    except Exception as e:
        print(e)
