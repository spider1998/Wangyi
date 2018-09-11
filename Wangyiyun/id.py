# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
import requests
import re
import os
from lxml import etree
import heapq
import collections
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetAlbum():
    urls="https://music.163.com/#/search/m/?id=1001&initial=65&s=%E5%91%A8%E6%9D%B0%E4%BC%A6&type=10"
    headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'_iuqxldmzr_=32; _ntes_nnid=dc7dbed33626ab3af002944fabe23bc4,1524151830800; _ntes_nuid=dc7dbed33626ab3af002944fabe23bc4; __utmc=94650624; __utmz=94650624.1524151831.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=94650624.1505452853.1524151831.1524151831.1524176140.2; WM_TID=RpKJQQ90pzUSYfuSWgFDY6QEK1Gb4Ulg; JSESSIONID-WYYY=ZBmSOShrk4UKH5K%5CVasEPuc0b%2Fq6m5eAE91jWCmD6UpdB2y4vbeazO%2FpQK%5CgiBW0MUDDWfB1EuNaV5c4wIJZ08hYQKDhpsHnDeMAgoz98dt%2B%2BFfhdiiNJw9Y9vRR5S4GU%2FziFp%2BliFX1QTJj%2BbaIGD3YxVzgumklAwJ0uBe%2FcGT6VeQW%3A1524179765762; __utmb=94650624.24.10.1524176140',
    'Host':'music.163.com',
    'Referer':'https://music.163.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    html = requests.get(urls,headers=headers)
    print html.text
    html1=etree.HTML(html.text)
    #html_data=html1.xpath('//div[@class="u-cover u-cover-alb3"]')[0]
    pattern = re.compile(r'<span title=(.*?) class ="msk"></span>')
    items = re.findall(pattern, html.text)
    print items
    cal=0
    # 首先删除这个文件，要不然每次都是追加
    if(os.path.exists("专辑信息.txt")):
        os.remove("专辑信息.txt")
    #删除文件避免每次都要重复写入
    if (os.path.exists("专辑歌曲信息.txt")):
        os.remove("专辑歌曲信息.txt")
    for i in items:
        cal+=1
        #这里需要注意i是有双引号的，所以需要注意转换下
        p=i.replace('"','')
        #这里在匹配里面使用了字符串，注意下
        pattern1=re.compile(r'<a href="/album\?id=(.*?)" class="tit f-thide s-fc0">%s</a>'%(p))
        id1= re.findall(pattern1,html.text)
    #   print("专辑的名字是:%s!!专辑的ID是%s:"%(i,items1))
        with open("专辑信息.txt",'a') as f:
            f.write("专辑的名字是:%s!!专辑的ID是%s \n:"%(i,id1))
            f.close()
            #GetLyric1(id1)
  #  print("总数是%d"%(cal))
    print("获取专辑以及专辑ID成功！！！！！")

if __name__ == '__main__':
    GetAlbum()

