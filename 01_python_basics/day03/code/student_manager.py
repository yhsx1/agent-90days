# 初始化学生字典
student = {}

# 输出提示信息
print("==== 学生成绩管理系统 ====")
print("1. 添加学生")
print("2. 查询成绩")
print("3. 修改成绩")
print("4. 删除学生")
print("5. 显示所有学生")
print("0. 退出系统")

# 主菜单循环
while True:
    print("==== 学生成绩管理系统 ====")
    command = int(input("请选择操作："))

    if command == 1:
        print("==== 添加学生 ====")
        name = input("请输入学生姓名：")
        score = int(input("请输入学生成绩："))
        if name in student:
            print("学生已存在！")
        elif score < 0 or score > 100:
            print("成绩无效！")
        else:
            student[name] = score
            print("添加成功！")
    elif command == 2:
        print("==== 查询成绩 ====")
        name = input("请输入学生姓名：")
        if name in student:
            print(f"{name}的成绩是：{student[name]}")
        else:
            print("学生不存在！")
    elif command == 3:
        print("==== 修改成绩 ====")
        name = input("请输入学生姓名：")
        score = int(input("请输入学生成绩："))
        if name in student:
            if score < 0 or score > 100:
                print("成绩无效！")
            else:
                student[name] = score
        else:
            print("学生不存在！")
    elif command == 4:
        print("==== 删除学生 ====")
        name = input("请输入学生姓名：")
        if name in student:
            student.pop(name)
        else:
            print("学生不存在！")
    elif command == 5:
        print("==== 显示所有学生 ====")
        if len(student) != 0:
            for name, score in student.items():
                print(f"{name}：{score}")
        else:
            print("暂无学生记录")
    elif command == 0:
        print("==== 退出系统 ====")
        print("退出成功！")
        break
    else:
        print("无效操作！")
