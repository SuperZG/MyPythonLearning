# <class 'function'>
# username 为:形式参数
def greeting_user(username):
    '''print simple hello to users'''
    print('Hello,', username, '!')



# 'Jack' : 是我们的实参
greeting_user('Jack')
greeting_user('Python Training')
greeting_user(4)
print(id(greeting_user))
print(type(greeting_user))