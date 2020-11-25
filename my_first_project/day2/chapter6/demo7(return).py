# return 默认返回空值 None
# return 标志着函数的结束
# pass 就是占位符,防止空函数报错的,后面的代码可以继续使用
# f(x) =  b
def print_word():
    return
    print("hello")


a = print_word()
# None
print(a)
# <class 'NoneType'>
print(type(a))