# global 声明一个全句变量后,就可以在函数中对全局变量进行更改
# username = "xiaoming"
#
# def greeting_user():
#     global username
#     username = "xiaomei"
#     '''print simple hello to users'''
#     print('Hello,', username, '!')
#
#
# print(username)
# greeting_user()
# print(username)
# global 声明一个全句变量后,就可以在函数中对全局变量进行更改
username = "xiaoming"

def greeting_user(username):
    username = "xiaomei"
    '''print simple hello to users'''
    print('Hello,', username, '!')


print(username)
greeting_user(username)
print(username)