import requests
import webbrowser

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
        else:
            print("请选上面有的")      
    musicId = input("请输入要解析的音乐id>>>>>>>:")
    params={
        "type":musicType,
        "id":musicId
    }
    res = requests.get(url,params)
    res = res.json()
    print(res)
    return res

def showMusicHtml():
    res = music_analysis()
    print(res)
    # word = "<h1>{}</h1>".format(res.get("name"))
    # with open("music.html","w") as f:
    #     f.write(word)
            