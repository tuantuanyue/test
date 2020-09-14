# salary = int(input("请输入你的工资："))
# if salary <= 1000:
#     print("老板，我是你爹！")
# elif salary > 1000 and salary <= 2000:
#     print("老板，wqnmlgbxxxx")
# elif salary > 2000 and salary <= 5000:
#     print("老板脑子有坑，背后说坏话。")
# elif salary > 5000 and salary <= 10000:
#     print("老板说的有点问题，但我不说话。")
# elif salary > 10000 and salary <= 20000:
#     print("老板说啥就是啥把，给钱就行！")
# elif salary >20000 and salary <= 30000:
#     print("老板说什么都是对，如果有人错了，那一定是我。")
# elif salary >30000 and salary <=50000:
#     print("996就像呼吸一样自然。")
# else:
#     print("公司就是我家。")


# score = int(input("请输入你的成绩："))
# while score > 100 or score < 0:
#     if score > 100:
#         print("请输入0-100的数字！")
#         score = int(input("请输入你的成绩："))
#     elif score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >= 60:
#         print("C")
#     elif score >= 40:
#         print("D")
#     elif score >= 0:
#         print("E")
#     else:
#         print("请输入0-100的数字！")
#         score = int(input("请输入你的成绩："))



# for i in range(1,6):
#     print(f"-----{i}层-------")
#     if i == 3:
#             continue
#     for j in range(1,8):
#         if i == 4 and j == 4:
#             print("遇到鬼屋了，OVER了")
#             break
#         print(f"L{i}--{i}0{j}")


for i in range(1,11):
    if i <= 5:
        print("*"*i)
    else:
        print("*"*(10-i))
        