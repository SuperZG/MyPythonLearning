squares = (100, 80)
print(squares)
# squares[0] = 200  # 错误的赋值
print(squares[0])  # 可以索引引用

# demo = ()
# length = (1)
# print(type(length))  # type 为对象类型 <class 'int'>，把括号当成数学运算的括号
# print(type(demo))  # type 为对象类型 <class 'tuple'>
# width = (2,)  # 单个对象,不能省略
# print(type(width))  # <class 'tuple'>

inner = (10, 20, 30)
outer = ('hello', 'hola', inner)
print(outer)
print(outer[2][2])



list = [1,2,3]
# 复杂类型,存储元素,实际上存储的是他的内存地址.
# 作为元组的元素的list,值改变时,地址不变.
# 对于元组而言,它的地址就不变
a = (10, 20, list)
print(id(a))
print(a)
a[2][1] = 3
print(id(a))
print(a)



