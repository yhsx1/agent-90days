# 获取姓名和年龄
name = input("请输入姓名：")
age = int(input("请输入年龄："))

# 判断是否成年
if age >= 18:
    print(f"{name}，你已经成年了")
else:
    print(f"{name}，你还未成年")