# sum = 0
# x = 0
# while x <= 100:
#     sum = sum + x
#     x = x + 1
# print(sum)


prompt = 'Type in anything, it will be repeated.\
\nIf you want to quit, type in "quit".\
\nInput: '
flag = True
while flag:
    input("这是第一层循环")
    while flag:
        message = input(prompt)
        if message == 'quit':
            # flag = False
            # break 可以跳出当前层的循环,无视标识位,但不会让所有层循环都终止
            break
        else:
            print(message)

print('This is the end of the loop')
