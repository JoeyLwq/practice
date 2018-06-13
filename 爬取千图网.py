#__author: Joey
#date:    2018/5/18

import urllib.request
import re
import urllib.error
import os

for i in range(1,2):
    url='http://www.58pic.com/tupian/biyedabian-808-0-%d.html' %i
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')


    opener=urllib.request.build_opener()   #创建一个opener对象
    opener.addheader=[headers]

    urllib.request.install_opener(opener)  #安装该opener对象到全局

    data=urllib.request.urlopen(url).read().decode('gbk','ignore')

    pattern = re.compile(r'<div class="flow-item.*?<img.*?src="(http://.*?).jpg!qt324',re.S)
    images = re.findall(pattern,data)

    for j in range(0,len(images)):
        try:
            image = images[j] + '.jpg!'
            print(image)
            file = os.path.join(os.path.abspath('.'), str(i) + str(j) + '.jpg')
            urllib.request.urlretrieve(image,file)
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
        except Exception:
            print(Exception.__name__)

