# 获取用户输入
n = int(input("请输入一个正整数："))

# 初始化累加变量
total = 0

# 判断输入是否有效并使用 for 循环累加
if n <= 0:
    print("请输入正整数！")
else:
    for i in range(1, n + 1):
        total += i

    # 输出结果
    print(f"1 到 {n} 的整数之和为：{total}")