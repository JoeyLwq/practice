#__author: Joey
#date:    2018/5/18

import urllib.request
import re
cursor = 6402316859476902656
url=r'https://video.coral.qq.com/varticle/2657538333/comment/v2?callback=_varticle2657538333commentv2&orinum=10&oriorder=o&pageflag=1&cursor=%d&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1526631351246' %cursor
headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')

opener=urllib.request.build_opener()   #创建一个opener对象
opener.addheader=[headers]

urllib.request.install_opener(opener)  #安装该opener对象到全局

for i in range(0,5):
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    pattern_content = re.compile(r'"content":"(.*?)",',re.S)
    contents = re.findall(pattern_content,data)

    for j in range(0,len(contents)):
        try:
            print(eval('u"'+contents[j]+'"'))   #  u"something"
        except UnicodeEncodeError:
            continue

    pattern_next = re.compile(r'"last":"(.*?)"',re.S)
    next_cursor = int(re.findall(pattern_next,data)[0])
    print(next_cursor)
    url = r'https://video.coral.qq.com/varticle/2657538333/comment/v2?callback=_varticle2657538333commentv2&orinum=10&oriorder=o&pageflag=1&cursor=%d&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1526631351246' %next_cursor
