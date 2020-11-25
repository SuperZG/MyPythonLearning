# 上下文管理器,用with...as方法创建的对象,会在代码块运行完的时候进行关闭
# I love Python
# I love Java too
# And you?
# with open('D:\\inout9\\text1', 'r') as example:
#     # print(example.read())
#     # 在不关闭的情况下,数字参数表示继续读几个字符
#     # I love Python
#     print(example.readline())
#     # ['I love Java too\n', 'And you?']
#     print(example.readlines())

# encoding='gbk'
# 鎴戠埍Python
# 鎴戜篃鐖盝ava
# And you?

# encoding='utf-8'
# 我爱Python
# 我也爱Java
# And you?

with open('D:\\inout9\\text1',encoding='utf-8') as example:
    print(example.read())
