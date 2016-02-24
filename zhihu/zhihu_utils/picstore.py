# -*- coding: utf-8 -*-
import urllib
import os

imgurl = 'http://pic3.zhimg.com/4acf2eab97e5e42ff438c9b84fa5fbba.jpg'

name = os.path.basename(imgurl)

pic = urllib.request.urlopen(imgurl)

with open('../../static/zhihuimg/','wb') as f:
    f.pipe(pic.read())