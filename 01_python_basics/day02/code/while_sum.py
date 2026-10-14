# 获取用户输入
n = int(input("请输入正整数："))

# 使用 while 验证正整数
while n <= 0:
    print("输入无效，请重新输入")
    n = int(input("请输入正整数："))

# 使用 for 循环求和
total = 0

for i in range(1, n + 1):
    total += i

print(f"1 到 {n} 的整数之和为：{total}")