# -*- coding:utf-8 -*-
import re
import json
while 1:
    string=input()
    if string=='END':
       break
    t=string[0]
    t2=t+'!'
    string=string.replace(t2,'')#删除！
    string=string.replace('.','')#删除句号
    name=(re.findall(r"(.*),",string))[0]#找出姓名
    string=string.replace(name,'')#剔除姓名
    number=(re.findall(r"\d{11}",string))[0]#找出电话号码
    string=string.replace(number,'')#剔除电话号码
    string=string.replace(',','')#剔除，
    import cpca
    list1=[]
    df=cpca.transform([string])
    df=df.values
    province=df[0][0]
    city=df[0][1]
    qu=df[0][2]
    if city=="北京市":
        province="北京"
    if city == "天津市":
        province = "天津"
    if city=="上海市":
        province="上海"
    if city=="重庆市":
        province="重庆"
    list1.append(province)
    list1.append(city)
    list1.append(qu)
    leave=df[0][3]
    first=[""]
    second=[""]
    thild=[""]
    forth=""
    fifth=""
    #街道/镇/乡
    x='街道'
    y='镇'
    z='乡'
    if  leave.find(x)>0:
        first=(re.findall(r".*街道",leave))#找出街道
        leave=leave.replace(first[0],"")
    elif leave.find(y)>0:
        first = (re.findall(r".*镇", leave))  # 找出镇
        leave = leave.replace(first[0], "")
    elif leave.find(y)>0:
        first = (re.findall(r".*乡", leave))  # 找出乡
        leave = leave.replace(first[0], "")
    list1=list1+first
    list2=list1
    if(t=='1'):
        list1.append(leave)
        print(json.dumps(dict((("姓名", name), ("手机", number), ("地址", list1))), ensure_ascii=False))
    else:
        x='街'
        y='巷'
        z='路'
        p='胡同'
        q='弄'
        if leave.find(x)>0:
            second=(re.findall(r".*街",leave))#找出街或大街
            leave=leave.replace(second[0],"")
        elif leave.find(y)>0:
            second = (re.findall(r".*巷", leave))  # 找出巷
            leave = leave.replace(second[0], "")
        elif leave.find(z)>0:
            second = (re.findall(r".*路", leave))  # 找出路
            leave = leave.replace(second[0], "")
        elif leave.find(z)>0:
            second = (re.findall(r".*胡同", leave))  # 找出路
            leave = leave.replace(second[0], "")
        elif leave.find(z)>0:
            second = (re.findall(r".*弄", leave))  # 找出路
            leave = leave.replace(second[0], "")
        list2=list2+second
        x='号'
        if leave.find(x)>0:
            thild=(re.findall(r"\d*号",leave))#找出门牌号
            leave=leave.replace(thild[0],"")
        list2=list2+[thild[0]]
        list2.append(leave)
        print(json.dumps(dict((("姓名", name), ("手机", number),("地址",list2))),ensure_ascii=False) )
