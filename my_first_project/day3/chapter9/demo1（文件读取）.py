# 读取文件
# 默认参数为mode为'r' 是读取的意思
# open就是文件的打开
# example = open('D:\\inout9\\text1')
# # example就是文件对象
# str = example.read()
# print(type(str))  # <class 'str'>
# print(str)
# # 相当于文件的关闭
# example.close()


# 上下文管理器,用with...as方法创建的对象,会在代码块运行完的时候进行关闭
with open('D:\\inout9\\text1', 'r') as example:
    # print(example.read())
    # 在不关闭的情况下,数字参数表示继续读几个字符
    print(example.read(5))
    print(example.read(5))
    print(example.read(5))
    print(example.read(5))
