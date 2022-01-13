import json
import datetime
import re
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView

from article.models import article
from users.models import userProfile
from webData.serializer import userDataSerializer


def websiteData(request):
    nowUserNumber = userProfile.objects.count()
    nowArticleNumber = article.objects.filter(~Q(title='欢迎新人')).count()
    recentLogTime = User.objects.filter(
        username=request.session.get('username')).first().last_login
    a = datetime.datetime(2021, 7, 10)
    b = datetime.datetime.now()
    b.strftime('%Y/%m/%d %H:%M:%S')
    newArticles = article.objects.filter(~Q(title='欢迎新人') & Q(
        createTime__gt=datetime.datetime.now().date())).count()
    newUsers = article.objects.filter(Q(title='欢迎新人') & Q(
        createTime__gt=datetime.datetime.now().date())).count()
    data = {'code': 200, 'msg': '查询网页数据成功', 'websiteOperationTime': (b - a).days, 'nowUserNumber': nowUserNumber,
            'recentLogTime': recentLogTime, 'newArticles': newArticles, 'nowArticleNumber': nowArticleNumber,
            'newUsers': newUsers}
    return JsonResponse(data)


def douBanHotMovie(request):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=80'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    # page = response.text
    # print(page)
    dicObj = response.json()
    # fp = open('filename.json', 'w', encoding='utf-8')
    # json.dump(dicObj, fp=fp, ensure_ascii=False)
    # print(dicObj)
    data = {'code': 200, 'msg': '获取豆瓣热门成功', 'content': dicObj}
    return JsonResponse(data)


def weibo(request):
    url = "https://s.weibo.com/top/summary"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
        "Cookie": "SINAGLOBAL=3367921994550.5557.1569889839988; SUB=_2AkMo4xN5f8NxqwJRmfoUxWvkao12ywzEieKev-KiJRMxHRl-yT9jqkwZtRB6A2M9lgpAeTr_lsVvzlYYGAtpPTduQyxn; UOR=www.baidu.com,weibo.com,www.baidu.com; _s_tentry=-; Apache=6822011594630.65.1634468878367; ULV=1634468878377:2:1:1:6822011594630.65.1634468878367:1614934577441"}
    wb_response = requests.get(url, headers=headers)
    webcontent = wb_response.text
    soup = BeautifulSoup(webcontent, "html.parser")
    index_list = soup.find_all("td", class_="td-01")
    title_list = soup.find_all("td", class_="td-02")
    level_list = soup.find_all("td", class_="td-03")

    topic_list = []
    for i in range(len(index_list)):
        item_index = index_list[i].get_text(strip=True)
        if item_index == "":
            item_index = "0"
        item_title = title_list[i].a.get_text(strip=True)
        if title_list[i].span:
            item_mark = title_list[i].span.get_text(strip=True)
        else:
            item_mark = "置顶"
        item_level = level_list[i].get_text(strip=True)
        topic_list.append({"index": item_index, "title": item_title, "mark": item_mark, "level": item_level,
                           "link": f"https://s.weibo.com/weibo?q=%23{item_title}%23&Refer=top"})
        data = {'code': 200, 'msg': '获取微博热门成功', 'content': topic_list}
    return JsonResponse(data)


def zhihu(request):
    headers = {"User-Agent": "", "Cookie": ''}
    zh_url = "https://www.zhihu.com/billboard"
    zh_response = requests.get(zh_url, headers=headers)
    webcontent = zh_response.text
    soup = BeautifulSoup(webcontent, "html.parser")
    script_text = soup.find("script", id="js-initialData").get_text()
    rule = r'"hotList":(.*?),"guestFeeds"'
    result = re.findall(rule, script_text)
    temp = result[0].replace("false", "False").replace("true", "True")
    hot_list = eval(temp)
    data = {'code': 200, 'msg': '获取知乎热门成功', 'content': hot_list}
    return JsonResponse(data)


class userData(APIView):
    def get(self, request):
        nowUser = userProfile.objects.filter(user=User.objects.get(
            username=request.session.get('username'))).first()
        nowUserDataSerializer = userDataSerializer(nowUser)
        data = {'code': 200, 'msg': '查询个人数据成功',
                'nowUserDataSerializer': nowUserDataSerializer.data}
        return JsonResponse(data)
