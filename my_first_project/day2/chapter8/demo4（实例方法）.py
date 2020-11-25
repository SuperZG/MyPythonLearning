class Student():
    def __init__(self, name, score):  # 类、方法之间的空格已省略
        self.name = name
        self.score = score

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
    hellen.print_score()
    print(hellen.get_grade())
