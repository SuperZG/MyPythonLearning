# <class 'set'> 集合
# 集合可以理解为字典的键值，没有VALUE
# set_1 = set([1, 2, 4, 3, 3, 2, 1]) #用set函数将一个list转化为set
# print(set_1)
# print(type(set_1))
# # 内置方法add添加一个元素
# set_1.add(5)
# set_1.add(4)
# print(set_1)
# # 内置方法remove删除一个元素
# set_1.remove(2)
# print(set_1)


set_1 = {1, 2, 3, 4}
set_2 = set([1, 3, 5, 7])
print(type(set_1))
print(set_2)
# # 交集
# set_and = set_1 & set_2
# print(set_and)
# # 并集
# set_or = set_1 | set_2
# print(set_or)

# 不能用[]取值,默认取的是value值
# print(set_1[1])
