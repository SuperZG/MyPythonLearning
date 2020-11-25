# 参数前面加*，代表为可变长参数，可以接收tuple，可变参数也必须放在必选参数的后面，*号的意思是创建一个名为numbers的空元组来接收实参。
def calcu(*numbers):
    print(numbers)
    print(type(numbers))
    sum = 0
    for number in numbers:
        sum = sum + number * number
    print('The sum answer is:', sum)


# calcu(1, 2, 3, 4)
numlist = [2, 4, 6, 8]
# calcu(numlist)
calcu(*numlist)
'''
(2, 4, 6, 8)
<class 'tuple'>
The sum answer is: 120

'''
#不加星号的话，也可以直接传递list或者tuple，不过必须将list和tuple传入1个变量传入。。
def calcu(numbers):
    print(numbers)
    print(type(numbers))
    sum = 0
    for number in numbers:
        sum = sum + number * number
    print('The sum answer is:', sum)


# calcu(1, 2, 3, 4)  #calcu() takes 1 positional argument but 4 were given
numlist = (2, 4, 6, 8)
# calcu(numlist)
calcu(numlist)

'''
[2, 4, 6, 8]
<class 'list'>
The sum answer is: 120
'''
