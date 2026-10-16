# 计算平均分
def calculate_average(scores):
    # 初始化总成绩
    total = 0

    # 循环计算总成绩
    for score in scores:
        total += score

    # 返回平均分
    return total / len(scores)

# 获取成绩等级
def get_grade(score):
    if score < 0 or score > 100:
        grade = "无效"
    elif score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"

    # 返回成绩等级
    return grade

# 输出学生成绩报告
def print_student_report(name, score, subject="Python"):
    # 获取成绩等级
    grade = get_grade(score)

    # 输出学生成绩报告
    print(f"姓名：{name}\n课程：{subject}\n成绩：{score}，等级：{grade}")

if __name__ == '__main__':
    # 成绩列表
    scores = [85, 92, 76, 88, 95]

    # 班级成绩统计
    average = calculate_average(scores)
    print("==== 班级成绩统计 ====")
    print(f"班级平均分：{average:.2f}")
    print()

    # 学生成绩报告
    print("==== 学生成绩报告 ====")
    print_student_report("小明", 95)
    print()
    print("==== 学生成绩报告 ====")
    print_student_report(name="小红", score=88, subject="AI Agent")
    print()

    # 异常成绩检查
    print("==== 异常成绩检查 ====")
    print(f"成绩 105 的等级：{get_grade(105)}")