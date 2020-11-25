import makeinfos


# __name__特点:
# 在本模块内,__name__返回一个__main__
# 在其他模块内(在被调用的时候),__name__返回那个模块的模块名

# 通过__name__属性的特点,我们可以判断代码是被调用还是在本模块
# 就可以通过if判断,避免部分代码被调用

# makeinfos
# __main__
print(makeinfos.__name__)
print(__name__)