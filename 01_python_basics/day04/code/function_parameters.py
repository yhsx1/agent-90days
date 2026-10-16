# 定义 greet_student(name)
def greet_student(name):
    print(f"你好，{name}，欢迎学习 Python 函数！")

# 定义 calculate_sum(a, b)
def calculate_sum(a, b):
    return a + b

# 定义 calculate_average(a, b, c)
def calculate_average(a, b, c):
    return (a + b + c) / 3

if __name__ == '__main__':
    # 接收学生姓名，输出欢迎信息
    greet_student("小明")

    # 接收两个整数，计算它们的和
    total = calculate_sum(10, 20)
    print(f"两个整数的和：{total}")

    # 接收三个成绩，计算平均分
    average = calculate_average(85, 90, 95)
    print(f"三个成绩的平均分：{average:.2f}")

    # 使用函数返回值
    print(f"总和的两倍：{total * 2}")

