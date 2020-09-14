
import time
import random
import pymysql

def jiafa(a,b):
    if type(a) is int and type(b) is int:
        print(a + b)
    else:
        print("请输入正确的数据类型！")


""" 
a = input("请输入你的名字：")
b = input("请输入你的年龄: ")
try:
    if int(b) >= 18:
        print(a,"成年了！")
    else:
        print(a,"未成年！")
except Exception as c:
    print("你上面的代码错了",c) """

""" 
for i in range(10):
    time.sleep(1)
    print(i) """



""" a = random.randint(0,100)
time.sleep(0.5)
print(a) """




""" def check(username,password):
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(password) >= 6 and len(password) <= 12:
                print("注册成功",{username,password})
            else:
                print("密码格式不正确，密码长度为6-12位！")
        else:
            print("账号第一位必须为小写字母！")
    else:
        print("你输入的账号不符合规范！第一位为小写字母且账号长度为5-8位！")

check("127642","dakdhaksd") """


""" class Car():
    def __init__(self,pinpai,yanse,neishi,jilun):
        self.pinpai = pinpai
        self.yanse = yanse
        self.neishi = neishi
        self.jilun = jilun
    def bianxing(self):
        print("车子变身金刚喜羊羊！")

    def fly(self):
        print("车子开始起飞！")

car = Car("baoma","yellow","haohua","4lun")
car.bianxing()
car.fly() """



# text = input("请输入今天的心情：")
# with open("日记.txt","w",encoding="utf8") as f:
#     f.write(text)

a = [["张三",90],["王大麻子",89],["李四",58],["李六",73],["赵八",88],["汪九",79],["曾二",66]]
print(a)

