import random

print("欢迎各位员工来到年会抽奖环节！下面将依次抽取三等奖30名：避孕套一盒，二等奖6名：iphone手机，一等奖3名：泰国5日游！")
for i in range(3):
    print(f"下面开始抽取{3-i}等奖！")
    three = []
    two = []
    one = []
    if i == 0:
        count3 = 0
        while count3 < 30:
            x = random.randint(1,301)
            if x not in three:
                three.append(x)
                print(x)
                count3 += 1
            else:
                pass
        print(f"恭喜三等奖获得者：{three}")
    elif i == 1:
        count2 = 0
        while count2 < 6:
            y = random.randint(1,301)  
            if y not in three and y not in two:
                two.append(y)
                print(y)
                count2 += 1
            else:
                pass
        print(f"恭喜二等奖获得者：{two}")
    else:
        count1 = 0
        while count1 < 3:
            z = random.randint(1,301)
            if z not in two and z not in three and z not in one:
                one.append(z)
                print(z)
                count1 += 1
            else:
                pass
        print(f"恭喜一等奖获得者：{one}")
