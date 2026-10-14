# 获取学生姓名和成绩
name = input("请输入学生姓名：")
score = int(input("请输入考试成绩："))

# 使用 if/elif/else 判断等级
if score < 0 or score > 100:
    print("成绩无效")
elif score >= 90:
    print(f"{name}的成绩为 {score} 分，等级：优秀")
elif score >= 80:
    print(f"{name}的成绩为 {score} 分，等级：良好")
elif score >= 60:
    print(f"{name}的成绩为 {score} 分，等级：及格")
else:
    print(f"{name}的成绩为 {score} 分，等级：不及格")