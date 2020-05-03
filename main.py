import aboutMe
import expression as E
import imgDownload
import music as M
import showlogo
import weather as W
import note as N
import texttable as table

def showMenu():
    selectList=[
        ["功能","选项"],
        ["记事本","1"],
        ["天气预报","2"],
        ["音乐解析器","3"],
        ["图片下载","4"],
        ["表情包生成","5"],
        ["关于我","6"],
        ["退出","7"]
    ]
    newTable = table.Texttable()
    newTable.add_rows(selectList)
    # print(help(table))
    print(newTable.draw())
    selectMenu()

def selectMenu():
    userSelect = 0
    while userSelect==0:
        userSelectM = input("请选择功能>>>>>:")
        if str(userSelectM) == '1':
            print("="*20+"记事本"+"="*20)
            N.note()
        elif str(userSelectM) == '2':
            print("="*20+"天气预报"+"="*20)
            W.get_weather()
        elif str(userSelectM) == '3':
            print("="*20+"音乐解析"+"="*20)
            M.showMusicHtml()
        elif str(userSelectM) == '4':
            print("图片下载")
        elif str(userSelectM) == "5":
            print("="*20+"表情包生成"""+"="*20)
            word = input("请输入你在表情包上生成的字>>>>>>>>>:")
            E.genImage(word)   
        elif str(userSelectM) == '6':
            print("关于我")        
        elif str(userSelectM) == '7':
            userSelect=1 
        else:
            print("请选上面有的")
            userSelect==0

if __name__ == "__main__":
    showlogo.showlogo()
    showMenu()