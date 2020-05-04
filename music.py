import requests
import webbrowser
import os
import main

def music_analysis():
    url = "https://api.toubiec.cn/rand.music"
    select = 0
    print('='*20)
    print("1,网易云音乐")
    print("2,腾讯音乐")
    print("3,退出")
    print("="*20)
    musicApp = input("请选择要解析的音乐平台>>>>>>:")
    musicType = ''
    while select==0:
        if str(musicApp) == '1':
            musicType = "netease"
            select = 1                
        elif str(musicApp) == '2':
            musicType = "tencent"
            select = 1 
        elif str(musicApp) == "3":
            select = 1
            return main.showMenu()
        else:
            print("请选上面有的")      
    musicId = input("请输入要解析的音乐id>>>>>>>:")
    params={
        "type":musicType,
        "id":musicId
    }
    res = requests.get(url,params)
    res = res.json()
    return res

def createHtml(word):
    with open("music.html","w") as f:
        f.write(word)
    webbrowser.open_new_tab("music.html")    
    print("歌曲解析保存在"+str(os.path.abspath('music.html')))    

def showMusicHtml():
    res = music_analysis()
    res = res.get('data')
    lrcData= ''
    if res.get("name") == "解析失败 参数错误":
        return print("请输入正确参数")    
    if not res.get('lrc_data'):
        lrcData="暂无歌词"
    else:
        lrcData=res.get("lrc_data")  
    htmlWord = """
    <h1 style="text-align: center;">{name}</h1>
    <p style="text-align: center;">{author}</p>
    <div style="width: 100%;text-align: center;">
        <img src="{pic}"
            style="text-align: center;display:block;margin: 0 auto;">
        <audio
            src="{url}"
            controls='controls'></audio>
        <h3>歌词</h3>    
        <textarea name="" id="" cols="30" rows="10" style="display: block;margin: 0 auto;">
            {lrc_data}
        </textarea> 
    """.format(name=res.get('name'),author=res.get('author'),pic=res.get('pic'),lrc_data=lrcData,url=res.get('url'))

    createHtml(htmlWord)
           