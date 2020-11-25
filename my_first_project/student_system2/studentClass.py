class Student(object):

    def __init__(self, id, name, gender, tel):
        self.__id = id
        self.__name = name
        self.__gender = gender
        self.__tel = tel

    @property
    def id(self):
        return self.__id

    @property
    def gender(self):
        return self.__gender

    @property
    def name(self):
        return self.__name

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def __str__(self):
        return "{id:%s,name:%s,gender:%s,tel:%s}" % (self.__id, self.__name, self.__gender, self.__tel)
