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
        # 实例属性前面加__表示该属性为私有属性，无法在外面更改，只能通过属性方法更改。
        # 实例属性前面加_表示该属性应该为私有属性，不过你可以看
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    # 重写str方法，可以打印我们想要的值，print(对象名)
    def __str__(self):
        str = "%s得了%s分" % (self.__name, self.__score)
        return str

    # 实例方法
    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.score >= 85:
            return 'A'
        elif self.score >= 70:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    xiaoming = Student('xiaoming', 90)
    xiaoming.name = "xiaomei"
    xiaoming.score = "91"
    print(xiaoming.get_name())
    print(xiaoming.get_score())
