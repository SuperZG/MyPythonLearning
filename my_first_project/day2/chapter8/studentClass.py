class Student(object):
    # 类属性:类的每一个对象都共有的属性,不需要每次单独定义
    logo = "少先队"

    # 类方法:可以调用类属性的方法
    @classmethod
    def is_shaoxiandui(cls):
        print("%d去上学" % cls.logo)

    # 静态方法:既不调用类属性,又不调用实例属性(没有cls和self)
    @staticmethod
    def love_study():
        print()

    # 实例化方法,有self的方法
    def __init__(self, name, score):  # 类、方法之间的空格已省略
        # 实例属性
        self.name = name
        self.score = score

    #重写str方法，可以打印我们想要的值，print(对象名)
    def __str__(self):
        str = "%s得了%s分" % (self.name, self.score)
        return str

    # 实例方法
    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 85:
            return 'A'
        elif self.score >= 70:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    hellen = Student('Hellen Evans', 85)
    # xiaoming = Student('xiaoming', 90)
    # ['__class__',
    # '__delattr__',
    # '__dict__',
    # '__dir__',
    # '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_grade', 'is_shaoxiandui', 'logo', 'love_study', 'name', 'print_score', 'score']
    # dir 返回对象所有的内置属性和方法
    print(dir(hellen))
    print(hellen)
