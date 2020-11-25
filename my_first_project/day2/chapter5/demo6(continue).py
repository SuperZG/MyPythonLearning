# continue 可以跳过当前一次循环,一般和if语句配合使用
names = ['Alice', 'Bob', 'Dave', 'Mark', 'Jason']
for name in names:
    if name == 'Dave' or name == 'Mark':
        continue
    print('Hello!', name)
