class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('\n%s:%s' % (self.name, self.age))


class Teacher(SchoolMember):
    # 父类的同名方法再次改写,称为方法的"重写"
    # 重写的方法会覆盖掉父类的方法,在使用时从子类开始找,找到则只会用重写的方法,找不到就用父类的
    # def __init__(self, name, age, salary):
    #     SchoolMember.__init__(self, name, age)
    #     self.salary = salary

    # 另外一种方式重写父类方法，适用于接受所有其他形参而不用一个个标识出来
    def __init__(self, salary, *args, **kwargs):
        self.salary = salary
        super().__init__(*args, **kwargs)

    def print_info(self):
        print(
            '\nName:', self.name,
            '\nAge:', self.age,
            '\nSalary:', self.salary
        )


class Student(SchoolMember):
    pass


if __name__ == '__main__':
    xiaoming = Student("小明", 18)
    wang = Teacher("王老师", 30, 5000)
    # wang.print_info()
    # xiaoming.print_info()
    print(dir(xiaoming))
    print(dir(wang))
