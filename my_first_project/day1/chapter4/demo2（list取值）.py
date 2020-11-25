# 嵌套的取值
names = [['Alice', 'Alison'], ['Dave', 'David'], ['Mark', 'Maggie']]
print(names)
print(names[0][0])
print(names[2][-1])

# 列表的切片
# list[start:stop:step]
whole_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(whole_list)
# print(whole_list[0:8:2])
# print(whole_list[:10:3])
# print(whole_list[5::2])
# step默认为1
print(whole_list[2:4:])
print(whole_list[12:])
print(whole_list[:5])
print(whole_list[::4])
# -1代表反向
print(whole_list[::-2])

