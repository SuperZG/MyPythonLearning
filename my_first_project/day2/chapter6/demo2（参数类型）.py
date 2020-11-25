def max_num(a, b): #a,b形参
    '''This function will compare the input\
 and print the bigger number out.'''
    if a > b:
        print(a, 'is the maximum number.')
    elif a == b:
        print(a, 'equals to', b, '.')
    else:
        print(b, 'is the maximum number.')


max_num(5, 7) #5,7在这里就是实参
# x = 110
# y = 110
# max_num(x, y)
# max_num(b=12, a=5)
