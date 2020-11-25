with open('D:\\inout9\\multi2.txt', 'w') as example:
    flag = True
    while flag:
        message = input('Input anything, quit to exit:\n')
        if message == 'quit':
            flag = False
        else:
            message = message + '\n'
            example.write(message)

with open('D:\\inout9\\multi2.txt', 'r') as exampleread:
    print(exampleread.read())
