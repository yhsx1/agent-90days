# 第一部分：元组操作

# 创建元组
student = ("小明", 24, "计算机科学与技术")

# 输出完整元组
print(student)

# 使用索引输出姓名和专业
print(f"姓名：{student[0]}")
print(f"专业：{student[-1]}")

# 元组解包
name, age, subject = student

# 输出学生信息
print(f"学生信息：{name}，{age} 岁，{subject}")

# 第二部分：集合操作

# 创建集合
skills_a = {"Python", "Java", "Git"}
skills_b = {"Python", "C++", "Git"}

# 集合的交集、并集和差集
print(f"{skills_a} 和 {skills_b} 的交集为：{skills_a & skills_b}")
print(f"{skills_a} 和 {skills_b} 的并集为：{skills_a | skills_b}")
print(f"{skills_a} 和 {skills_b} 的差集为：{skills_a - skills_b}")

# 集合添加和删除元素
print(f"修改前的集合为：{skills_a}")
skills_a.add("Docker")
skills_a.discard("Java")
print(f"修改后的集合为：{skills_a}")

# 判断元素是否在集合中
print(f"Python 是否在集合中：{'Python' in skills_a}")