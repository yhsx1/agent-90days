# 定义欢迎函数
def show_welcome():
    print("==== AI Agent 学习系统 ====")
    print("欢迎进入 Day 4 Python 函数学习")

# 定义菜单函数
def show_menu():
    print("==== 学习菜单 ====")
    print("1. 学习 Python")
    print("2. 学习 AI Agent")
    print("0. 退出系统")

if __name__ == '__main__':
    # 输出程序启动信息
    print("系统启动中...")

    # 调用欢迎函数
    show_welcome()

    # 调用菜单函数
    show_menu()
    show_menu()

    # 输出程序结束信息
    print("程序运行结束")