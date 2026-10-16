# 定义全局变量
school = "AI Agent 学习系统"
name = "全局小明"

# 定义 show_info()
def show_info():
    name = "局部小红"
    print("==== 函数内部信息 ====")
    print(f"学校：{school}")
    print(f"姓名：{name}")

# 定义 calculate_square(number)
def calculate_square(number):
    result = number ** 2

    return result

if __name__ == '__main__':
    # 调用信息显示函数内部信息
    show_info()

    # 调用平方函数
    result = calculate_square(6)

    # 输出函数外部信息
    print("==== 函数外部信息 ====")
    print(f"姓名：{name}")
    print(f"6 的平方：{result}")
    print(f"学校：{school}")