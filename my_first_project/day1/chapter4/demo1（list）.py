# names = ['Alice', 'Bob', 'Dave', 'Mark', 'Dave', 'Jason']
# 索引号： 0          1          2            3           4
#         -5        -4         -3           -2          -1
# print(names)
# print(id(names))
#
# print(names[0])
# print(names[3])
# print(names[-1])
# print(names[-3])

# 对第3个索引位的元素进行重新赋值
# names[3] = 'Kevin'
# print(names)
# 同一个列表对象,元素更改后,id不改变
# print(id(names))

# <class 'list'> 空列表的定义
nums = []
# 1.append方法更改list,返回一个None
nums.append(1)
nums.append(1)
nums.append(1)
print(nums)
print(type(nums))

# 2.insert方法 添加一个元素,在指定位置
# 使用-1时,最后一位还会后移
# names.insert(-1,"xiaoming")
# print(names)

# 3.pop 方法,默认删除最后一个元素
# 方法可以添加参数,参数为要删除元素的索引
# names.pop(1)
# print(names)

# 4.del删除
# print(names)
# del names[2]
# print(names)

# 5.remove方法
# print(names)
# names.remove('Dave')
# print(names)
# names.remove('Dave')
# print(names)

# 6.extend方法,拼接一个复杂数据类型
# names = ['Alice', 'Bob', 'Dave']
# print(names)
# names.extend(['Mark', 'Jason'])
# names.extend(('Mark', 'Jason'))
# print(names)
