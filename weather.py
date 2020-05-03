import requests
import urllib
import texttable as table

def get_weather():
    serachCity = input("请输入要查询的城市>>>>>>")
    city = {"city":"{}".format(serachCity)}
    url = "http://wthrcdn.etouch.cn/weather_mini"
    res = requests.get(url,city)
    if res.status_code == 200:
        if res.json().get("desc") == "invilad-citykey":
            return print("无效的城市")
        newTable  = table.Texttable()
        newList = [
            ["城市","最高气温","风力","天气","风向","最低温度","日期"]
        ]
        list2 = []
        res = res.json().get("data")
        for con in res.get("forecast"):
            list2=[res.get("city"),con.get("high"),con.get('fengli'),con.get("type"),con.get("fengxiang"),con.get("low"),con.get("date")]
            newList.append(list2)

        newTable.add_rows(newList)
        print(newTable.draw())            
    else:
        print("查询失败")
    