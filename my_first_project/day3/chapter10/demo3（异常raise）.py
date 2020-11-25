# 继承了Exception,并重写了init方法
# Exception 是所有异常类的基类
class InputShort(Exception):
    '''User defined exception error class'''

    def __init__(self, length, minimum):
        Exception.__init__(self)
        self.length = length
        self.minimum = minimum


if __name__ == '__main__':
    try:
        text = input('Please input anything: ')
        if len(text) < 3:
            # raise 后面接一个异常对象
            raise InputShort(len(text), 3)
        # others will continue as usual
    except EOFError:
        print('You input Ctrl+D')
    #     as生成了一个临时对象
    except InputShort as insh:
        print('InputShort: The input was %d long, expected at least %d long' %
              (insh.length, insh.minimum))
    else:
        print('Your input: ', text)
