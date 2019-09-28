import re
import cpca
import numpy
import pandas
import json

while 1:
    str1 = input()
    if str1 == 'END':
        break
    xian = str1.split('!')
    list1 = xian[1].split(',')
    shuchuan = re.findall("[0-9]+", str(list1[1]))
    mark = 0
    for i in range(len(shuchuan)):
        if len(shuchuan[i]) == 11:
            mark = 1
            break
    if mark == 1:
        list2 = list1[1].split(re.findall("[0-9]{11}", str(list1[1]))[0])
        teph = re.findall("[0-9]{11}", str(list1[1]))[0]
        adr = list2[0] + list2[1]
        adr1 = adr[:-1]
    else:
        teph = "未找到正确号码"
        adr = list1[1]
        adr1 = adr[:-1]
    list3 = adr1.split('.')
    df = cpca.transform(list3, cut=False)
    df = df.values
    pvee = df[0][0].split('省')
    pve = pvee[0]
    if pve == '北京市':
        pve = '北京'
    elif pve == '天津市':
        pve = '天津'
    elif pve == '上海市':
        pve = '上海'
    elif pve == '重庆市':
        pve = '重庆'
    if adr1.find(pve, 0, len(pve)) == -1:
        df = cpca.transform(list3)
        df = df.values
    pve = df[0][0]
    if pve == '北京市':
        pve = '北京'
    elif pve == '天津市':
        pve = '天津'
    elif pve == '上海市':
        pve = '上海'
    elif pve == '重庆市':
        pve = '重庆'
    sell = df[0][1]
    cot = df[0][2]
    de_ad = df[0][3]

    if len(de_ad.split('镇', 1)) > 1:
        si_ji = de_ad.split('镇', 1)
        de1 = si_ji[0] + '镇'
        de2 = si_ji[1]
    elif len(de_ad.split('乡', 1)) > 1:
        si_ji = de_ad.split('乡', 1)
        de1 = si_ji[0] + '乡'
        de2 = si_ji[1]
    elif len(de_ad.split('街道', 1)) > 1:
        si_ji = de_ad.split('街道', 1)
        de1 = si_ji[0] + '街道'
        de2 = si_ji[1]
    elif len(de_ad.split('民族乡', 1)) > 1:
        si_ji = de_ad.split('民族乡', 1)
        de1 = si_ji[0] + '民族乡'
        de2 = si_ji[1]
    elif len(de_ad.split('苏木', 1)) > 1:
        si_ji = de_ad.split('苏木', 1)
        de1 = si_ji[0] + '苏木'
        de2 = si_ji[1]
    elif len(de_ad.split('南山区', 1)) > 1:
        si_ji = de_ad.split('南山区', 1)
        de1 = si_ji[0] + '南山区'
        de2 = si_ji[1]
    else:
        de1 = ""
        de2 = de_ad

    if xian[0] == '1':
        a_list = [pve, sell, cot, de1, de2]
        dict1 = {"姓名": list1[0], "号码": teph, "地址": a_list}
        print(json.dumps(dict1, ensure_ascii=False))
    else:
        list4 = re.findall("[0-9]+['号', '弄']", de2)
        escp = re.findall("['街', '路', '道', '胡同', '弄', '巷'][0-9]+['号', '弄']", de2)
        if len(list4):
            list5 = de2.split(list4[0])
            if len(escp):
                de3 = list5[0]
                de4 = list4[0]
                de5 = list5[1]
            else:
                escp1 = re.findall("['街', '路', '道', '胡同', '弄', '巷']", de2)
                list6 = de2.split(escp1[0])
                de3 = list6[0] + escp1[0]
                de4 = ""
                de5 = list6[1]
        else:
            escp1 = re.findall("['街', '路', '道', '胡同', '弄', '巷']", de2)
            if len(escp1):
                list6 = de2.split(escp1[0])
                de3 = list6[0] + escp1[0]
                de4 = ""
                de5 = list6[1]
            else:
                de3 = ""
                de4 = ""
                de5 = de2

        a_list = [pve, sell, cot, de1, de3, de4, de5]
        dict1 = {"姓名": list1[0], "手机": teph, "地址": a_list}
        print(json.dumps(dict1, ensure_ascii=False))
