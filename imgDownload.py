import os
import requests
import gzip
import random
import json
import time
import urllib
import main
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import texttable

fake_user = UserAgent()
headers = {"User-Agent": fake_user.random}
url = "http://pic.netbian.com/"

def selectCount():
    count = input("您想下载几张？(单次下载不得超过20张)>>>>>>>>>:")
    if(count.isdigit()==False):
        print("请正确输入")
        return selectCount()
    while int(count)>20:
        print("请正确输入")
        return selectCount()
    return count

def folder():
    if not os.path.exists("images"):
        os.mkdir("images")

def userSerach():
    userS = input("请选择你想要的图片类型>>>>>>>>>:")
    return userS

def getTypePage(pararm,page="index.html"):
    res = requests.get(url+str(pararm)+str(page),headers=headers)
    # print(res.content)
    # res = res.text
    # print(type(res.content))
    res = res.content.decode('gbk')
    return res

def downloadImage(num,count,pararm):
    folder()
    imageList = []
    page = "index_{}.html".format(random.randint(2,num))
    res = getTypePage(pararm,page)
    soup = BeautifulSoup(res,'lxml')
    image = soup.select('#main > div.slist > ul > li > a')
    # print(image)
    for key in range(count):
        print("正在下载第{}张图片".format(key+1))
        # print(image[key].get('href'))
        res2 = requests.get(url+str(image[key].get('href')))
        res2 = res2.content.decode('gbk')
        soup2 = BeautifulSoup(res2,'lxml')
        item = soup2.select('#img > img')
        # print(item[0].get("src"))
        img = urllib.request.urlopen(url+str(item[0].get("src")))
        with open("images/{}.jpg".format(str(time.time())+str(item[0].get("alt"))),"wb") as f:
            f.write(img.read())    
    print("下载完成")
    print("图片保存在"+str(os.path.abspath('images')))            
    # title = soup.select('#main > div.slist > ul > li > a > b')
    # for key in count:
    #     image[0].get('src')
    # print(json.loads(image[0]).get("src"))
    # print(title)
    # for key in range(count):
    #     with open(url+str(image[key].get('src')))
    
    
    


def webPageCount(res):
    # num1,num2=''
    num1 = 0
    num2 = 0
    soup = BeautifulSoup(res,'lxml')
    pageCount = soup.select('#main > div.page > a')
    # print(soup)
    # print(image,title)
    # print(pageCount)
    for tag in pageCount:
        if tag.text != '下一页':
            num2 = int(tag.text)
            if int(num2)>int(num1):
                num1 = int(num2)
            else:
                pass

    return num1        
    # print(num1)        
    # print(pageCount[1].text)
    # print(pageCount)
    # print(len(pageCount))
   


def userSelect(choose):
    print(choose)
    selectd = 0
    while selectd == 0:
        if str(choose) == '1':
            pararm = "4kfengjing/"
            selectd=1
        elif str(choose) == '2':
            pararm = "4kmeinv/"
            selectd=1
        elif str(choose) == '3':
            pararm = "4kyouxi/"
            selectd=1
        elif str(choose) == '4':
            pararm = "4kdongman/"
            selectd=1                
        elif str(choose) == '5':
            pararm = "4kyingshi/"
            selectd=1
        elif str(choose) == '6':
            pararm = "4kmingxing/"
            selectd=1
        elif str(choose) == '7':
            pararm = "4kqiche/"
            selectd=1
        elif str(choose) == '8':
            pararm = "4kdongwu/"
            selectd=1
        elif str(choose) == '9':
            pararm = "4krenwu/"
            selectd=1
        elif str(choose) == '10':
            pararm = "4kmeishi/"
            selectd=1
        elif str(choose) == '11':
            pararm = "4kzongjiao/"
            selectd=1
        elif str(choose) == '12':
            pararm = "4kbeijing/"
            selectd=1
        elif str(choose) == '13':
            pararm = "4kbeijing/"
            selectd = 1
            main.showMenu()
        else:
            print("请输入正确选项")
            return userSerach()       
    return pararm


def ImgMenu():
    table = texttable.Texttable()
    imgTypes =[
        ["图片类型","选项"]
    ]
    selectMenu ={
        "1":"风景",
        "2":"美女",
        "3":"游戏",
        "4":"动漫",
        "5":"影视",
        "6":"明星",
        "7":"汽车",
        "8":"动物",
        "9":"人物",
        "10":"美食",
        "11":"宗教",
        "12":"背景",
        "13":"退出"
    }
    for key in selectMenu:
        imgTypes.append([selectMenu[key],key])

    table.add_rows(imgTypes)
    print(table.draw())
    

def imgMain():
    ImgMenu()
    userS = userSerach()
    pararm = userSelect(userS)
    res = getTypePage(pararm)
    num = webPageCount(res)
    count = selectCount()
    downloadImage(num,int(count),pararm)
    
    
