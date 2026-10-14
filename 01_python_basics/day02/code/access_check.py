# 获取用户信息
name = input("请输入姓名：")
age = int(input("请输入年龄："))
is_active = input("账号是否已激活（yes/no）：")

# 将账号转移状态转换为布尔值
is_active = is_active == "yes"

# 判断年龄是否合法以及是否具备访问权限
if age < 0 or age > 120:
    print("年龄输入无效")
elif not is_active:
    print(f"{name}，账号未激活，禁止访问")
elif age >= 18:
    print(f"{name}，允许访问 AI 系统")
else:
    print(f"{name}，未达到访问年龄要求")