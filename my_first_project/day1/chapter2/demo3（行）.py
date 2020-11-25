# 每物理行对应一个逻辑行
value = 100
print(id(value))
value = value + 100
print(id(value))
print(value)
# 一个物理行表示多个逻辑行用;分割
value = 100;value = value + 100;print(value);
# 多个物理行表示一个逻辑行用\连接
words = 'this is a long string. \
it will be ended in the second physical line.'
print(words)
