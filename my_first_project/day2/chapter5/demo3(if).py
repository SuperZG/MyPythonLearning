value_got = input('Please input your age: ')
age = int(value_got)
if age >= 18:
    print('Your age is:', age)
    print('Adult')
else:
    print('Your age is:', age)
    print('Non-adult')

# value_got = input('Please input your age: ')
# age = int(value_got)
# if age < 4:
#     print('Entrance price is free')
# elif age < 18:
#     print('Entrance price is $5')
# elif age < 28:
#     print('Entrance price is $7')
# else:
#     print('Entrance price is $10')

# in:判断左边的值是否是一个复杂数据结构的元素
names = ['Alice', 'Bob', 'Dave', 'Mark', 'Jason']
# names1 = ('Alice', 'Bob', 'Dave', 'Mark', 'Jason')
# names2 = {'Alice':'Bob', 'Dave': 'Mark'}
# names3 = {'Alice', 'Bob', 'Dave', 'Mark', 'Jason'}
new_name = input('Please input a name: ')
if new_name in names:
    print('%s already in the list' % new_name)
else:
    print('%s not in the list' % new_name)


