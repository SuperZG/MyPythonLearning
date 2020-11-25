# str内置方法join,用指定的字符串连接我们的列表
phase = "This's a sample phase into a list"
phase_list = list(phase)
print(phase_list)
cut_1 = phase_list[9:15]
print(cut_1)
style_1 = ''.join(cut_1)			# 组合时不用任何字符
style_2 = '-'.join(cut_1)			# 组合时使用”-”字符
print(style_1)
print(style_2)


# str类型的切片
# print(phase[0])
# print(phase[0:2])
# print(phase[0::2])

