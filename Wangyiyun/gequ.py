# !/usr/bin/python
# coding=utf-8
# @author:spider1998
import requests
from time import sleep
import re
import os
import glob
import json
from lxml import etree
import heapq
import collections
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

global song

class Getword():
    def GetAlbum(self):
        urls="http://music.163.com/artist/album?id=6452&limit=100&offset=0"
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
        html1=etree.HTML(html.text)
        html_data=html1.xpath('//div[@class="u-cover u-cover-alb3"]')[0]
        pattern = re.compile(r'<div class="u-cover u-cover-alb3" title=(.*?)>')
        items = re.findall(pattern, html.text)
        cal=0
        # 首先删除这个文件，要不然每次都是追加
        if(os.path.exists("专辑信息.txt")):
            os.remove("专辑信息.txt")
        #删除文件避免每次都要重复写入
        if (os.path.exists("专辑歌曲信息.txt")):
            os.remove("专辑歌曲信息.txt")
        print "开始加速拉取资源并写入本地......"
        for i in items:
            cal+=1
            #这里需要注意i是有双引号的，所以需要注意转换下
            p=i.replace('"','')
            #这里在匹配里面使用了字符串，注意下
            pattern1=re.compile(r'<a href="/album\?id=(.*?)" class="tit s-fc0">%s</a>'%(p))
            id1= re.findall(pattern1,html.text)
        #   print("专辑的名字是:%s!!专辑的ID是%s:"%(i,items1))
            with open("专辑信息.txt",'a') as f:
                f.write("专辑的名字是:%s!!专辑的ID是%s \n:"%(i,id1))
                f.close()
                self.GetLyric1(id1)
      #  print("总数是%d"%(cal))
        print("所有专辑，专辑ID,歌曲，歌曲ID爬取成功！！！！！\n  ")
        sleep(3)
        print "所有文件写入成功"





    def GetLyric1(self,id1):
        urls1 = "http://music.163.com/#/album?id="
        urls2 = str(id1).replace("[","").replace("]","").replace("'","").replace("u","")
        urls3= urls1+urls2
        #将不要需要的符号去掉
        urls=urls3.replace("#/","")
        headers={
            'Cookie': '_ntes_nuid=59954b250ada17a1ed5236518ca3a531; _ntes_nnid=40ac8db785679c5a47c6d0dbd1f446e7,1534505001088; hb_MA-94A1-BB29DC5DA865_source=www.hao123.com; mp_MA-94A1-BB29DC5DA865_hubble=%7B%22sessionReferrer%22%3A%20%22http%3A%2F%2Flove.163.com%2F%22%2C%22updatedTime%22%3A%201534505828031%2C%22sessionStartTime%22%3A%201534505828026%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%201%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%2218d92f05-7b99-4356-ae17-659f104ffad0%22%2C%22persistedTime%22%3A%201534505828023%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201534505828031%7D%2C%22sessionUuid%22%3A%20%221ede1187-8d34-4eb8-b890-d6b56a57e748%22%7D; _iuqxldmzr_=32; __utmc=94650624; __utma=94650624.133010862.1536369462.1536369462.1536369462.2; __utmz=94650624.1536369462.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=t39IC4W0U8HgZhfvgh1KxZzjgcIRvMF6; WM_NI=KC0De7WhebJEEoixIWzkgF9O%2FGt4WztNYV%2BK2cn4UIDNZbJr2pdI4Nm%2B9UPgM9GLU6oKbipIvdMGQKr0cZzvO1Qac0%2Ff5mJ6u%2B%2FGsOij09fdLnq883jyAp8ikriZbyKvSnM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb7e8738b89f8b1d76ba7b989a8eb7a90bbbebbc541a3b797a8c94790a7e58ee72af0fea7c3b92a899d00a5e83d95b8ab83c94f87b1a799cc5dbab5a9a7bc45ed99bcd5d672b89297b7aa41f2bda2d5d84388929683c97af2b0acaab746aff5f7b6d36d8fe789add83ead95ae8af343b6bc83a8d441b2f0adbbf97e8def9f82e23cedbafb8ec93eb7f5e1a8f245abb600dae57090b2bfd9bb39aaa78f91bb63a9aea7bbe17389aa9d8fd037e2a3; JSESSIONID-WYYY=%5CEtReHPZOrK1ueHX37sOs5NvaF8W0HwHFyA9vfNJnmEyo910GVn080BjIYHNR7anJ5frIMHfhe%2BRUpw0u%2BYtpajiRTnaDhdfwX90mj6kD0AVbhSSmSRWnPJna6%2Fo05AXwV8u%2FzaDV0IfOYeoolxfeejrX7AUEWK%2BuJ6E1s1wCwddmZO4%3A1536378224952; __utmb=94650624.112.10.1536369462',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }
        html = requests.get(urls, headers=headers)
        html1 = etree.HTML(html.text)
       # soup = BeautifulSoup(html1, 'html.parser', from_encoding='utf-8')
       # tags = soup.find_all('li', class_="have-img")
        html_data = html1.xpath('//ul[@class="f-hide"]//a')
        for i in html_data:
            #注意这个用法
            html_data1=i.xpath('string(.)')
            #获取歌曲的id
            html_data2=str(html_data1)
            pattern1=re.compile(r'<a href="/song\?id=(\d+?)">%s</a>'%(html_data2.decode("utf-8")))
            items = re.findall(pattern1,html.text)
            #print("歌曲的名称为: %s"%(html_data2))
            #print("歌曲的id为: %s"%(items))
            with open("专辑歌曲信息.txt", 'a') as f:
                #print(len(items))
                if (len(items) > 0):
                    f.write("歌曲的名字是: %s!!歌曲的ID是%s \n" % (html_data2, items))
                    f.close()
                #print("获取歌曲 %s 以及歌曲的ID %s写入文件成功"%(html_data2, items))
            #http://music.163.com/#/song?id=185617
               # if(len())




    def GetLyric2(self):
        # 首先删除原来的文件，避免重复写入
        for i in glob.glob("*热评*"):
            os.remove(i)
        for i in glob.glob("*歌曲名*"):
            os.remove(i)
        # 直接读取所有内容
        file_object = open("专辑歌曲信息.txt", )
        list_of_line = file_object.readlines()
        aaa = 1
        namelist = ""
        print "正在从互联网拉取资源..."
        for i in list_of_line:
            # 歌曲的名字是: 同一种调调!!歌曲的ID是['186020']
            pattern1 = re.compile(r'歌曲的名字是: (.*?)!!歌曲的ID是')
            pattern2 = re.compile(r'歌曲的ID是\[(.*?)\]')
            items1 = "".join(re.findall(pattern1, i)).replace("[", "").replace("]", "").replace("'", "")
            items2 = str(re.findall(pattern2, i)).replace("[", "").replace("]", "").replace('"', "").replace("'", "").replace("u", "")

            headers = {
                'Request URL': 'http://music.163.com/weapi/song/lyric?csrf_token=',
                'Request Method': 'POST',
                'Status Code': '200 OK',
                'Remote Address': '59.111.160.195:80',
                'Referrer Policy': 'no-referrer-when-downgrade'
            }
            #      http://music.163.com/api/song/lyric?id=186017&lv=1&kv=1&tv=-1
            urls = "http://music.163.com/api/song/lyric?" + "id=" + str(items2) + '&lv=1&kv=1&tv=-1'
            #     urls = "http://music.163.com/api/song/lyric?id=186018&lv=1&kv=1&tv=-1"
            # print(urls)
            html = requests.get(urls, headers=headers)
            json_obj = html.text
            j = json.loads(json_obj)
            try:
                lrc = j['lrc']['lyric']
                pat = re.compile(r'\[.*\]')
                lrc = re.sub(pat, "", lrc)
                lrc = lrc.strip()
                lrc = str(lrc)
                with open("歌曲名-" + items1 + ".txt", 'w') as f:
                    f.write(lrc)
                aaa += 1
                namelist = namelist + items1 + ".txt" + ","
                # 调用获取评论方法，并且把热评写入文件
                self.GetCmmons(items1, items2)
            except:
                #print("歌曲有错误 %s !!" % (items1))
                pass
            # 读取所有文件，并且把所有的信息输入到一个文件里面去
        # html1 = etree.HTML(html.text)
        print("歌曲一共爬取了%s首... " % (aaa))
        sleep(1)
        print "等待歌词及热评写入完毕......"
        sleep(3)
        print "写入完毕..."
        print "所有信息获取完毕，即将开始歌手分析..."
        #print(namelist)


    def GetCmmons(self,name,id):
        self.name=name
        self.id=id
        #删除原来的文件 避免重复爬取
        for i in glob.glob("hotComment"):
            os.remove(i)
      #  urls="http://music.163.com/weapi/v1/resource/comments/R_SO_4_415792918?csrf_token="
        urls="http://music.163.com/api/v1/resource/comments/R_SO_4_"+str(id)
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_iuqxldmzr_=32; _ntes_nnid=dc7dbed33626ab3af002944fabe23bc4,1524151830800; _ntes_nuid=dc7dbed33626ab3af002944fabe23bc4; __utmz=94650624.1524151831.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=RpKJQQ90pzUSYfuSWgFDY6QEK1Gb4Ulg; JSESSIONID-WYYY=BgqSWBti98RpkHddEBZcxnxMIt4IdbCqXGc0SSxKwvRYlqbXDAApbgN%2FQWQ8vScdXfqw7adi2eFbe30tMZ13mIv9XOAv8bhrQYC6KRajksuYWVvTbv%2BOu5oCypc4ylh2Dk5R4TqHgRjjZgqFbaOF73cJlSck3lxcFot9jDmE9KWnF%2BCk%3A1524380724119; __utma=94650624.1505452853.1524151831.1524323163.1524378924.5; __utmc=94650624; __utmb=94650624.8.10.1524378924',
            'Host': 'music.163.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }
        html = requests.get(urls,headers=headers)
        html.encoding= 'utf8'
      #  html_data = html1.xpath('//div[@class="u-cover u-cover-alb3"]')[0]
       # pattern = re.compile(r'<div class="u-cover u-cover-alb3" title=(.*?)>')
        #items = re.findall(pattern, html.text)
        #print(html.text)
        #使用json格式化输出
        json_obj = html.text
        j = json.loads(json_obj)
        i=j['hotComments']
        for uu in  i:
            username=uu["user"]['nickname']
            likedCount1 = str(uu['likedCount'])
            comments=uu['content']
            with open(name + "的热评hotComment" +".txt" , 'a+') as f:
                f.write("用户名是 "+username+"\n")
                f.write("用户的评论是 "+comments+"\n")
                f.write("被点赞的次数是  " + str(likedCount1) +"\n")
                f.write("----------华丽的的分割线-------------"+"\n")
                f.close()

    def MergedFile(self):
        for i in glob.glob("*allLyric*"):
            os.remove(i)
        aaa = 0
        for i in glob.glob("*歌曲名*"):
            file_object = open(i, 'r')
            list_of_line = file_object.readlines()
            for p in list_of_line:
                if "作词" in p or "作曲" in p or "混音助理" in p or "混音师" in p or "录音师" in p or "执行制作" in p or "编曲" in p or "制作人" in p or "录音工程" in p or "录音室" in p or "混音录音室" in p or "混音工程" in p or "Programmer" in p or p == "\n" or "和声" in p or "吉他" in p or "录音助理" in p or "陈任佑鼓" in p or song in p:
                    aaa += 1
                else:
                    with open("allLyric" + ".txt", "a") as f:
                        f.write(p)
                        f.write("\n")
        print("共过滤"+str(aaa)+"条无用数据")
        sleep(2)
        # 合并歌曲
        file1 = open('allLyric.txt', 'r')  # 要去掉空行的文件
        file2 = open('allLyric1.txt', 'w')  # 生成没有空行的文件
        try:
            for line in file1.readlines():
                if line == '\n':
                    line = line.strip("\n")
                file2.write(line)
        finally:
            file1.close()
            file2.close()
        print("合并歌词文件完成")




    def EmotionAnalysis(self):
        from snownlp import SnowNLP
        from pyecharts import Bar
        xzhou = []
        yzhou = []
        for i in glob.glob("*歌曲名*"):
            lis = []
            count = 0
            allsen = 0
            with open(i, 'r') as fileHandel:
                fileList = fileHandel.readlines()
                for p in fileList:
                    if "作词" in p or "作曲" in p or "鼓" in p or "混音师" in p or "录音师" in p or "执行制作" in p or "编曲" in p or "制作人" in p or "录音工程" in p or "录音室" in p or "混音录音室" in p or "混音工程" in p or "Programmer" in p or p == "\n":
                        pass
                    else:
                        s = SnowNLP(p)
                        #  print(s.sentences[0])
                        s1 = SnowNLP(s.sentences[0])
                        # print(type(s1))
                        count += 1
                        allsen += s1.sentiments
            if count == 0 or str(allsen) == 0:
                pass
            else:
                i = str(i)
                xzhou1 = i.split("-", 1)[1].split(".", 1)[0]
                xzhou.append(xzhou1)
                a = float(allsen)
                b = float(count)
                avg = a/b
                yzhou.append(avg)
                #print("%s这首歌的情绪为%s"%(i,avg))
                fileHandel.close()
        xzhou = ",".join(xzhou)
        xzhou = xzhou.split(",")
        bar = Bar("柱状图数据堆叠示例")
        bar.add("歌曲情绪可视化", xzhou, yzhou, is_stack=True, xaxis_interval=0)
        bar.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"歌曲情绪全部.html")
        # 显示最好的前五首歌
        import heapq

        yzhou1 = heapq.nlargest(10, yzhou)
        # print yzhou1
        # temp = map(yzhou.index, heapq.nlargest(10, yzhou))
        # temp = list(temp)
        yy = []
        for i in yzhou:
            yy.append(i)
        temp= []
        for i in range(10):
            temp.append(yy.index(max(yy)))
            yy[yy.index(max(yy))] = 0
        temp.sort()
        xzhou1 = []
        for i in temp:
            xzhou1.append(xzhou[i])
        # 情绪前十首歌个图
        bar = Bar("歌曲情绪较好前十首歌")
        bar.add("歌曲情绪可视化", xzhou1, yzhou1, is_stack=True, xaxis_interval=0)
        bar.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"歌曲最积极情绪top10.html")
        # 显示最差的十首歌
        yzhou1 = heapq.nsmallest(10, yzhou)
        temp = map(yzhou.index, heapq.nsmallest(10, yzhou))
        temp = list(temp)
        xzhou1 = []
        for i in temp:
            xzhou1.append(xzhou[i])
        # print(xzhou1)
        # print(yzhou1)
        # 情绪前十首歌个图
        bar = Bar("歌曲情绪较差前十首歌")
        bar.add("歌曲情绪可视化", xzhou1, yzhou1, xaxis_interval=0, xzhou1_label_textsize=6)
        bar.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"歌曲最消极情绪top10.html")



    def splitSentence(self,inputFile, outputFile):
        import jieba.analyse
        fin = open(inputFile, 'r')
        fout = open(outputFile, 'w')
        for line in fin:
            line = line.strip()
            line = jieba.analyse.extract_tags(line)
            outstr = " ".join(line)
            fout.write(outstr + '\n')
        fin.close()
        fout.close()
        #下面的程序完成分析前十的数据出现的次数
        f = open("分词过滤后.txt", 'r')
        a = f.read().split()
        b = sorted([(x, a.count(x)) for x in set(a)], key=lambda x: x[1], reverse=True)
        with open("分词词频.txt","w") as f:
            for k,v in b:
                f.write(k+str(v)+"\n")
        print "分词词频写入成功......"
        sleep(2)
        #print(sorted([(x, a.count(x)) for x in set(a)], key=lambda x: x[1], reverse=True))

    #输出频率最多的前十个字，里面调用splitSentence完成频率出现最多的前十个词的分析
    def LyricAnalysis(self):
        import jieba.analyse
        file = 'allLyric1.txt'
        #这个技巧需要注意
        alllyric = str([line.strip() for line in open('allLyric1.txt').readlines()])
    #获取全部歌词，在一行里面
        alllyric1=alllyric.replace("'","").replace(" ","").replace("?","").replace(",","").replace('"','').replace("?","").replace(".","").replace("!","").replace(":","")
       # print(alllyric1)
       #在这里用结巴分词来分词过滤并且输出到一个文件里面，这个ting.txt
       #import jieba.analyse 这里必须引入
        jieba.analyse.set_stop_words("ting.txt")
        self.splitSentence('allLyric1.txt', '分词过滤后.txt')
        #下面是词频统计
        import collections
        # 读取文本文件，把所有的汉字拆成一个list
        f = open("分词过滤后.txt", 'r')  # 打开文件，并读取要处理的大段文字
        txt1 = f.read().decode("utf-8")
        txt1 = txt1.replace('\n', '')  # 删掉换行符
        txt1 = txt1.replace(' ', '')  # 删掉换行符
        txt1 = txt1.replace('.', '')  # 删掉逗号
        txt1 = txt1.replace('.', '')  # 删掉句号
        txt1 = txt1.replace('o', '')  # 删掉句号
        txt1 = txt1.replace(r'e', '')  # 删掉yingwen
        mylist = list(txt1)
        mycount = collections.Counter(mylist)
        for key, val in mycount.most_common(10):  # 有序（返回前10个）
            with open(song+"词频统计10top.txt", "a") as f:
                f.write(key + str(val) + "\n")
            print "单字频率写入成功......"


    def Wordcloud(self):
        from pyecharts import WordCloud
        name = []
        value = []
        f = open("词频统计10top.txt", 'r')
        lines = f.readlines()
        for line in lines:
            li = line.strip().decode("utf-8")
            p = re.compile(ur'[^\u4e00-\u9fa5a-zA-z]')
            zh = "".join(p.split(li)).strip()
            zh = ",".join(zh.split())
            name.append(zh)
        for line in lines:
            pattern1 = re.compile(r"(\d+)")
            v = re.findall(pattern1,line)
            li = int(v[0])
            value.append(li)

        wordcloud = WordCloud(width=1300, height=620)
        wordcloud.add("", name, value, shape='diamond', word_size_range=[20, 100])
        wordcloud.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"歌词字云.html")


    def Hotimg(self):
        person = []
        for i in glob.glob("*歌曲名*"):
            f = open(i, 'r')
            lines = f.readlines()
            for line in lines:
                li = line.strip().decode("utf-8")
                if str(li).startswith("作词"):
                    p = li.split(":")[-1]
                    person.append(p)
        name = []
        num = []
        from collections import Counter
        li = Counter(person)
        for key, val in li.most_common(5):  # 有序（返回前10个）
            name.append(key)
            num.append(val)

        from pyecharts import Pie
        pie = Pie("作词人分布", title_pos='left', width=900, title_text_size=40)
        pie.add("作词人", name, num, center=[50, 50], is_random=False, radius=[30, 75], rosetype='area',
                is_legend_show=False, is_label_show=True, label_text_size=28)
        pie.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"作词人分布图.html")



    def MergedComment(self):
        for i in glob.glob("*hotcom*"):
            os.remove(i)
        aaa = 0
        for i in glob.glob("*热评*"):
            file_object = open(i, 'r')
            list_of_line = file_object.readlines()
            for p in list_of_line:
                if "用户名是" in p or "被点赞" in p or "华丽的" in p:
                    aaa += 1
                else:
                    p = p.split("用户的评论是 ")[-1].replace("首歌","").replace("周杰伦","").replace("杰伦","")
                    with open("hotcom" + ".txt", "a") as f:
                        f.write(p)
                        f.write("\n")
        print("共过滤"+str(aaa)+"条无用数据")
        sleep(2)
        # 合并歌曲
        file1 = open('hotcom.txt', 'r')  # 要去掉空行的文件
        file2 = open('hotcom1.txt', 'w')  # 生成没有空行的文件
        try:
            for line in file1.readlines():
                if line == '\n':
                    line = line.strip("\n")
                file2.write(line)
        finally:
            file1.close()
            file2.close()
        print("合并评论文件完成")



    def CsplitSentence(self,inputFile, outputFile):
        import jieba.analyse
        fin = open(inputFile, 'r')
        fout = open(outputFile, 'w')
        for line in fin:
            line = line.strip()
            line = jieba.analyse.extract_tags(line)
            outstr = " ".join(line)
            fout.write(outstr + '\n')
        fin.close()
        fout.close()
        #下面的程序完成分析前十的数据出现的次数
        f = open("热评分词过滤后.txt", 'r')
        a = f.read().split()
        b = sorted([(x, a.count(x)) for x in set(a)], key=lambda x: x[1], reverse=True)
        with open("热评分词词频.txt","w") as f:
            for k,v in b:
                f.write(k+str(v)+"\n")
        print "热评分词词频写入成功......"
        sleep(2)
        #print(sorted([(x, a.count(x)) for x in set(a)], key=lambda x: x[1], reverse=True))

    #输出频率最多的前十个字，里面调用splitSentence完成频率出现最多的前十个词的分析
    def CLyricAnalysis(self):
        for i in glob.glob("*热评分词*"):
            os.remove(i)
        import jieba.analyse
        file = 'allLyric1.txt'
        #这个技巧需要注意
        alllyric = str([line.strip() for line in open('hotcom1.txt').readlines()])
    #获取全部歌词，在一行里面
        alllyric1=alllyric.replace("'","").replace(" ","").replace("?","").replace(",","").replace('"','').replace("?","").replace(".","").replace("!","").replace(":","")
       # print(alllyric1)
       #在这里用结巴分词来分词过滤并且输出到一个文件里面，这个ting.txt
       #import jieba.analyse 这里必须引入
        jieba.analyse.set_stop_words("ting.txt")
        self.CsplitSentence('hotcom1.txt', '热评分词过滤后.txt')
        #下面是词频统计
        import collections
        # 读取文本文件，把所有的汉字拆成一个list
        f = open("热评分词过滤后.txt", 'r')  # 打开文件，并读取要处理的大段文字
        txt1 = f.read().decode("utf-8")
        txt1 = txt1.replace('\n', '')  # 删掉换行符
        txt1 = txt1.replace(' ', '')  # 删掉换行符
        txt1 = txt1.replace('.', '')  # 删掉逗号
        txt1 = txt1.replace('.', '')  # 删掉句号
        txt1 = txt1.replace('o', '')  # 删掉句号
        txt1 = txt1.replace(r'e', '')  # 删掉yingwen
        mylist = list(txt1)
        mycount = collections.Counter(mylist)
        for key, val in mycount.most_common(10):  # 有序（返回前10个）
            with open(song+"热评词频统计10top.txt", "a") as f:
                f.write(key + str(val) + "\n")
        print "热评单字频率写入成功......"



    def CWordcloud(self):
        from pyecharts import WordCloud
        name = []
        value = []
        f = open("热评分词词频.txt", 'r')
        lines = f.readlines()
        i = 1
        j = 1
        for line in lines:
            li = line.strip().decode("utf-8")
            p = re.compile(ur'[^\u4e00-\u9fa5a-zA-z]')
            zh = "".join(p.split(li)).strip()
            zh = ",".join(zh.split())
            name.append(zh)
            if i == 10:
                break
            i += 1
        for line in lines:
            pattern1 = re.compile(r"(\d+)")
            v = re.findall(pattern1,line)
            li = int(v[0])
            value.append(li)
            if j == 10:
                break
            j += 1

        wordcloud = WordCloud(width=1300, height=620)
        wordcloud.add("", name, value, shape='diamond', word_size_range=[20, 100])
        wordcloud.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"热评词云.html")



    def CHotimg(self):
        person = []
        tit = []
        num = 0
        for i in glob.glob("*的热评hot*"):
            title = i.title()
            t = title.split("的")[0]
            tit.append(t)
            h = 0
            p = 0
            f = open(i, 'r')
            lines = f.readlines()
            for line in lines:
                li = line.strip().decode("utf-8")
                if str(li).startswith("被点赞"):
                    p = int(li.split("  ")[-1])
                    h += p
                    num += p
            person.append(h)
        ttop = []
        import heapq
        ntop = heapq.nlargest(5, person)
        yy = []
        for i in person:
            yy.append(i)
        temp = []
        for i in range(5):
            temp.append(yy.index(max(yy)))
            yy[yy.index(max(yy))] = 0
        for t in temp:
            ttop.append(tit[t])

        from pyecharts import WordCloud,Bar

        bar = Bar("柱状图数据堆叠")
        bar.add("总计："+str(num), tit, person, is_stack=True, xaxis_interval=0)
        bar.render(r"/tmp/pycharm_project_120/Wangyiyun/result/" + song + "All所有歌曲热评点赞表.html")

        # wordcloud = WordCloud(width=1300, height=620)
        # wordcloud.add("", ttop, ntop, shape='diamond', word_size_range=[20, 100])
        # wordcloud.render(r"/tmp/pycharm_project_120/Wangyiyun/result/" + song + "歌曲热评点赞top5云图.html")
        # from pyecharts import Pie
        # pie = Pie("热评Top5", title_pos='left', width=500, title_text_size=20)
        # pie.add("被点赞", ttop, ntop, center=[50, 50], is_random=False, radius=[30, 75], rosetype='area',
        #         is_legend_show=False, is_label_show=True, label_text_size=28)
        # pie.render(r"/tmp/pycharm_project_120/Wangyiyun/result/"+song+"歌曲热评点赞Top5.html")









if __name__ == '__main__':
    # global song
    song = "周杰伦"
    g = Getword()
    # print "开始所有爬取专辑及歌曲信息..."
    # sleep(1)
    # g.GetAlbum()
    # print "开始爬取歌词及热评..."
    # sleep(2)
    # g.GetLyric2()
    # print "开始数据分析......"
    # sleep(2)
    # print "合并文件...."
    # sleep(2)
    # g.MergedFile()
    # print "开始情绪分析......"
    # g.EmotionAnalysis()
    # g.LyricAnalysis()
    # print "即将开始云词图绘制"
    # sleep(2)
    # g.Wordcloud()
    # print "云图绘制完毕......"
    # sleep(2)
    # print "开始绘制作词人分布图......"
    # g.Hotimg()
    # sleep(2)
    # print "即将开分析评论......"
    # sleep(2)
    # print "合成评论......"
    # sleep(2)
    # g.MergedComment()
    # print "正在处理分析评论数据......"
    # sleep(2)
    # g.CLyricAnalysis()
    # print "开始绘制热评云图..."
    # sleep(2)
    # g.CWordcloud()
    print "点赞数统计......"
    sleep(2)
    print "数据清洗并绘制..."
    sleep(2)
    g.CHotimg()
    print "热评分析完毕......"





