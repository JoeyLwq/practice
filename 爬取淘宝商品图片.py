#__author: Joey
#date:    2018/5/16
import os
import urllib.request
import re
key = urllib.request.quote('马甲裙')
for i in range(0,2):
    scale = i*60
    url='https://s.taobao.com/list?q='+key+'&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&spm=a219r.lmn002.1000187.1&bcoffset=12&s='+str(scale)
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    opener=urllib.request.build_opener()   #创建一个opener对象
    opener.addheader=[headers]
    urllib.request.install_opener(opener)  #安装该opener对象到全局
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')

    pattern = re.compile(r'"picUrl":"(.*?)"',re.S)
    images = re.findall(pattern,data)
    for j in range(0,len(images)):
        image = 'http:'+images[j]
        file = os.path.join(os.path.abspath('.'), str(i) + str(j) + '.jpg')
        urllib.request.urlretrieve(image,filename=file)