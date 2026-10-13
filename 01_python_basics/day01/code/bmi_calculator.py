# BMI 计算器

# 获取用户输入
name = input("请输入姓名：")
height_cm = float(input("请输入身高（cm）："))
weight_kg = float(input("请输入体重（kg）："))

# 单位转换
height_m = height_cm / 100

# 计算 BMI
bmi = weight_kg / height_m ** 2

# 输出结果
print("==== BMI 计算结果 ====")
print(f"姓名：{name}")
print(f"身高：{height_cm} cm")
print(f"体重：{weight_kg} kg")
print(f"BMI：{bmi:.2f}")
print("======================")