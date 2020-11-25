class Tool(object): #object为每一个类的父类，可以称为基类。
    # 类属性
    count = 0

    # 类方法，一个装饰器下面可以创建多个类方法
    @classmethod
    def show_tool_count(cls):
        # cls 是对类的引用,此处等于Tool类
        print("工具对象现在有%d个" % cls.count)


    # 静态方法,类中没有参数的方法
    @staticmethod
    def noise():
        print("嗡嗡嗡")

if __name__ == '__main__':
    tool = Tool()
    print(tool.count)
    tool.show_tool_count()
    # Tool.show_tool_count()
    Tool.count
    tool.noise()
    # python 是一个动态语言,它的类和对象在创建之后,还可以动态修改，java不能动态修改。
    # Tool.age = 1