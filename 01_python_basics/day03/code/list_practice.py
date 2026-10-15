# 创建成绩列表
scores = [85, 92, 76, 88, 95]

# 输出首尾元素
print("==== 原始成绩 ====")
print(scores)
print(f"第一个成绩：{scores[0]}")
print(f"最后一个成绩：{scores[-1]}")

# 修改、添加和删除成绩
scores[2] = 80
scores.append(90)
scores.remove(88)

# 统计数量、最高分和最低分
print("==== 修改后的成绩 ====")
print(scores)
print(f"成绩数量：{len(scores)}")
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")

# 使用 for 循环计算总分与平均分
total = 0

for score in scores:
    total += score

print(f"总成绩：{total}")
print(f"平均分：{total / len(scores):.2f}")