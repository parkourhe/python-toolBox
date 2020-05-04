import showlogo
import sqlite3
import os
from PIL import Image

char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# def connect():
#     qq = '995758538'
#     name = "parkourhe"
#     emill = "995758538@qq.com"
#     with open("demo.jpg","rb") as f:
#         avatar = f.read()
#         print(avatar)
#         con = sqlite3.connect('aboutMe.db')
#         sql = '''insert into about values(:qq,:emill,:name,:avatar) '''
#         cursor = con.cursor()
#         cursor.execute(sql,{"name":name,"qq":qq,"emill":emill,"avatar":avatar})   
#     con.commit()
#     cursor.close()
    
def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return ''
    length =  len(char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return char[int(gray/unit)]

def outputImg(img):
    WIDTH = 30 # 字符画的宽
    HEIGHT = 50 # 字符画的高
    imageFile = Image.open(img)
    imageFile = imageFile.rotate(90)
    # imgw = int(imageFile.size[0]*0.5)
    # imgh = int(imageFile.size[1]*0.5)
    imageFile = imageFile.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""
    for w in range(WIDTH):
        for h in range(HEIGHT):
            txt += get_char(*imageFile.getpixel((w,h)))
        txt += '\n'
    return txt

def queryAbout():
    con = sqlite3.connect('aboutMe.db')
    sql = '''select * from about'''
    cursor = con.cursor()
    res = cursor.execute(sql)
    res = res.fetchall()
    con.commit()
    cursor.close()
    return res
    

def aMain():
    res = queryAbout()
    f =open('temp.jpg',"wb")
    f.write(res[0][3])
    f.close()
    txt = outputImg(os.path.relpath('temp.jpg'))
    print(showlogo.showlogo())
    print("作者:"+str(res[0][0]))
    print("邮箱:"+str(res[0][1]))
    print("联系qq:"+str(res[0][2]))
    print("="*50)
    print(txt)
    


