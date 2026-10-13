# 学生信息输入
name = input("请输入姓名：")
age = int(input("请输入年龄："))
height = float(input("请输入身高（cm）："))

# 打印学生信息
print("==== 学生信息 ====")
print(f"姓名：{name}")
print(f"年龄：{age} 岁")
print(f"身高：{height} cm")
print("==================")

# 打印变量类型
print(type(name))
print(type(age))
print(type(height))
