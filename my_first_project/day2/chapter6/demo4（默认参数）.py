# 在定义函数时默认参数,一定在放在必选参数后面
# 我们称函数括号为参数列表,里面的值为参数
def greeting(msg, age, times=1):  # 末尾形参可带默认值
    print(msg * times)
    print(age)


# greeting('Hello')  # 可省略带默认值的参数
greeting('Hola', 5,times=2)
greeting(msg="hello",times=2, age=1)
