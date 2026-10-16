# 显示系统主菜单
def show_menu():
    print("==== 学生成绩管理系统 V2 ====")
    print("1. 添加学生成绩")
    print("2. 查询学生成绩")
    print("3. 修改学生成绩")
    print("4. 删除学生成绩")
    print("5. 显示所有学生成绩")
    print("0. 退出系统")

# 成绩合法性判断
def is_valid_score(score):
    if score < 0 or score > 100:
        return False
    else:
        return True

# 添加学生成绩
def add_student(students):
    # 输出操作提示
    print("==== 添加学生成绩 ====")

    # 获取学生姓名和成绩
    name = input("请输入学生姓名：")
    score = int(input("请输入学生成绩："))

    # 添加学生成绩
    if is_valid_score(score):
        if name in students:
            print("学生成绩已存在，添加学生失败！")
        else:
            students[name] = score
            print("添加学生成绩成功！")
    else:
        print("成绩无效，添加学生成绩失败！")

# 查询学生成绩
def query_student(students):
    # 输出操作提示
    print("==== 查询学生成绩 ====")

    # 获取学生姓名
    name = input("请输入学生姓名：")

    # 查询学生成绩
    if name in students:
        print(f"{name}的成绩是：{students[name]}")
    else:
        print("学生不存在，查询学生成绩失败！")

# 修改学生成绩
def update_student(students):
    # 输出操作提示
    print("==== 修改学生成绩 ====")

    # 获取学生姓名和成绩
    name = input("请输入学生姓名：")
    score = int(input("请输入学生成绩："))

    # 修改学生成绩
    if is_valid_score(score):
        if name in students:
            students[name] = score
            print("修改学生成绩成功！")
        else:
            print("学生不存在，修改学生成绩失败！")
    else:
        print("成绩无效，修改学生成绩失败！")

# 删除学生成绩
def delete_student(students):
    # 输出操作提示
    print("==== 删除学生成绩 ====")

    # 获取学生姓名
    name = input("请输入学生姓名：")

    # 删除学生成绩
    if name in students:
        students.pop(name)
        print("删除学生成绩成功！")
    else:
        print("学生不存在，删除学生成绩失败！")

# 显示所有学生成绩
def show_all_students(students):
    # 输出操作提示
    print("==== 显示所有学生成绩 ====")

    # 显示所有学生成绩
    if students:
        for name, score in students.items():
            print(f"姓名：{name}，成绩：{score}")
        print("显示所有学生信息成功！")
    else:
        print("暂无学生记录！")

if __name__ == '__main__':
    # 创建学生成绩字典
    students = {}

    while True:
        # 显示系统主菜单
        show_menu()

        # 获取用户操作
        command = int(input("请选择操作："))

        # 执行不同操作
        if command == 1:
            add_student(students)
        elif command == 2:
            query_student(students)
        elif command == 3:
            update_student(students)
        elif command == 4:
            delete_student(students)
        elif command == 5:
            show_all_students(students)
        elif command == 0:
            print("==== 退出系统 ====")
            print("退出系统成功！")
            break
        else:
            print("无效操作！")