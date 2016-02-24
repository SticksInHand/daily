from django.shortcuts import render
from django.http import HttpResponse
import urllib
import json
import os


# Create your views here.
def home(request):
    url = 'http://news-at.zhihu.com/api/4/news/latest'  # 这是要请求的url
    res = urllib.request.urlopen(url)
    result = res.read()
    ret = json.loads(result.decode())

    post_list = ret['stories']
    post_list2 = ret['top_stories']

    datetime = ret['date']
    for i in post_list:
        name = os.path.basename(i['images'][0])
        pic = urllib.request.urlopen(i['images'][0])
        i['img'] = '/static/zhihu/img/'+name
        with open('./static/zhihu/img/'+name,'wb') as f:
            f.write(pic.read())

    for i in post_list2:
        print(i)
        name = os.path.basename(i['image'])
        pic = urllib.request.urlopen(i['image'])
        i['img'] = '/static/zhihu/img/'+name
        with open('./static/zhihu/img/'+name,'wb') as f:
            f.write(pic.read())

    # for i in post_list:
    #     print(i)
    #     contenturl = 'http://news-at.zhihu.com/api/4/news/%s' % (i['id'])
    #     print(contenturl)
    #     contentret = json.loads(urllib.request.urlopen(contenturl).read().decode())
    #     i['content'] = contentret['body']

    return render(request, 'zhihu.html', {"post_list": post_list, "date_time": datetime, "post_list2":post_list2})

    # return render(request, 'home.html', {"name" : "test"})
