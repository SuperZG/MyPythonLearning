
class SchoolMember(object):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def print_info(self):
        print('\n%s:%s' % (self._name, self.age))


class Teacher(SchoolMember):
    # 父类的同名方法再次改写,称为方法的"重写"
    # 重写的方法会覆盖掉父类的方法,在使用时从子类开始找,找到则只会用重写的方法,找不到就用父类的
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def print_info(self):
        print(
            '\nName:', self._name,
            '\nAge:', self.age,
            '\nSalary:', self.salary
        )


# 多态案例:
#     子类对象被调用方法时,先在子类中找,找不到再去父类中找
#     正是因为这个特点,让我们在代码开发时,不再需要更改源代码,而是首先考虑写一个子类
#     这样的代码实现,就是多态的提现
def print_info(schoolMember):
    schoolMember.print_info()


if __name__ == '__main__':
    li = SchoolMember("李老师", 28)
    wang = Teacher("王老师", 30, 5000)
    print_info(wang)
    print_info(li)
    # wang._name = "wang老师"
    # wang.print_info()
    