# 创建学生信息字典
student = {
    "name": "小明",
    "age": 24,
    "major": "计算机科学与技术",
    "score": 85,
}

# 输出学生信息字典
print("==== 原始学生信息 ====")
print(student)

# 输出学生的姓名、年龄和专业
print(f"姓名：{student['name']}")
print(f"年龄：{student['age']}")
print(f"专业：{student['major']}")

# 使用 get 查询字典指定键的值，不存在返回默认值
print(f"身高：{student.get('height', "未知")}")

# 修改、添加、删除键值对
student["score"] = 95
student["city"] = "北京"
student.pop("age")

# 输出修改后的学生字典
print("==== 修改后的学生信息 ====")
print(student)

# 遍历学生信息
print("==== 遍历学生信息 ====")
for key, value in student.items():
    print(f"{key}：{value}")

# 判断键是否在字典中
print(f"是否包含成绩字段：{'score' in student}")