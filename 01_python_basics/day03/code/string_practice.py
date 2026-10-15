# 获取并清理字符串
text = input("请输入英文字符串：")
text = text.strip()

# 输出长度、首尾字符和切片
print("==== 字符串分析结果 ====")
print(f"字符串长度：{len(text)}")
print(f"第一个字符：{text[0]}")
print(f"最后一个字符：{text[-1]}")
print(f"前三个字符：{text[0:3]}")

# 转换大小写
print(f"大写形式：{text.upper()}")
print(f"小写形式：{text.lower()}")

# 使用 for 遍历字符串
print("==== 逐字符输出 ====")
for char in text:
    print(char)