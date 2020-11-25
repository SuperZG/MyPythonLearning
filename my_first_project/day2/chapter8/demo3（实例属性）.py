class Student():
    # 实例方法就是参数列表中,有self的所有方法
    # __init__是一个特殊的实例方法,实例化实例属性的
    def __init__(self, name, score):
        # 对当前对象的引用
        # 此处name和score为实例属性
        self.name = name
        self.score = score

    def study(self):
        print("我爱学习",self.name)


hellen = Student('Hellen Evans', 18)
print(hellen.name)
print(hellen.score)
print(hellen.study())

# 动态语言在此处暴露一个缺点,没办法确定类中的属性是否定义
