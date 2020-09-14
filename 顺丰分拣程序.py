ku = [['王*龙',"北京市海淀区苏州街"],['庞*飞','北京市昌平区'],['孙*云','山东省济南市山东省济南市历下区'],['鞠*龙','山东省潍坊市玉清街'],['张*','山东省济南市兴港路']]
shandong = []
beijin = []

sheng = {}
for i in ku:
    if "北京市" in i[1]:
        beijin.append(i)
    elif "山东省" in i[1]:
        shandong.append(i)
    else:
        pass
sheng['北京市'] = beijin
sheng['山东省'] = shandong
print(shandong)
print(beijin)
print(sheng)