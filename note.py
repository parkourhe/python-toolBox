import time
import texttable as table
import main


def noteWrite():
    with open('note.txt',"a+") as note:
        timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("现在是"+str(timeNow))
        word = input("想说点什么么？>>>>>>:")
        try:
            note.write(str(timeNow)+"&"+word+"\n")
        except IOError:
            print("="*20+"记录失败，请重试"+"="*20)
        else:
            print("="*20+"记录成功"+"="*20)

def noteRead():
    try:
        f = open("note.txt","r")
    except IOError:
        print('='*20+"您还没有进行过任何写日志的操作，请先写日志"+'='*20)
    else:
        list1 = [[
            "时间","说说"
        ]]
        newTable = table.Texttable()
        content = f.readlines()
        for con in content:
            ele = con.split("&")
            ele[1] = ele[1].replace("\n", "")
            list1.append(ele)          
        # print(list1)
        newTable.add_rows(list1)   
        print(newTable.draw())    
        f.close()
        
            
def noteMenu():
    menuList =[
        [
            "读(看看自己都写了什么)","写(记录一下)","退出记事本"
        ],
        [
            "A","B","C"
        ]
    ]
    selectN = 0
    newTable = table.Texttable()
    newTable.add_rows(menuList)
    print(newTable.draw())  
    while selectN==0:
        select = input("请选择记事本操作>>>>:\n")
        if select.lower()=="a":
            noteRead()
        elif select.lower()=="b":
            noteWrite()
        elif select.lower() == "c":
            selectN = 1
            main.showMenu()
        else:
            print('='*20+"请选择有的哦"+'='*20)
def note():
    noteMenu()
    timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print("现在是"+str(timeNow))
    # print("想说点什么么？")

