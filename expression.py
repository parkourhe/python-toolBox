from PIL import Image,ImageDraw,ImageFont
import os
def genImage(word):
    imgPath = "muban.jpg"
    fontPath = "font.ttf"
    color='#000000'
    img = Image.open(imgPath)
    fontType = ImageFont.truetype(fontPath,40)
    draw = ImageDraw.Draw(img)
    fontWidth,fontHeight = draw.textsize(word,fontType)
    draw.text((img.width/2-fontWidth/2,img.height/1.15),word,color,fontType)
    try:
        img.save("output.jpg")
    except IOError:
        print("保存失败")
    else:
        print("表情包保存在:"+os.path.abspath('output.jpg'))
    img.show()
    