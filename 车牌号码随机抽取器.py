import random
import string

a = string.ascii_uppercase + string.digits
b = random.sample(a,5)
c = "".join(b)
d = random.choice(string.ascii_uppercase)

i = 0
while i < 3:
    i += 1
    car_num = []
    for j in range(19):
        b = random.sample(a,5)
        c = "".join(b)
        d = random.choice(string.ascii_uppercase)
        h_num = f"京{d}.{c}"
        car_num.append(h_num)
        print(f"京{d}.{c}")   
    s = input("请输入你选中的车牌号：")
    if s in car_num:
        exit(f"恭喜你选中心爱的车牌号：{s}")
    elif i == 3:
        print("你的次数已用尽，请缴费从新选择。")
    else:
        print("你输入的车票号不存在，请重新选择！")
