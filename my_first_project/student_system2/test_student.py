from student_system2.studentClass import Student

if __name__ == '__main__':
    xiaoming = Student(0, "小明", "男", "13333333333")
    xiaoming_str = xiaoming.__str__()
try:
    # 1.打开系统先读取
    file = open("studentData.txt")
    xiaoming_str = file.read()
    print(xiaoming)
except FileNotFoundError:
    file = open("studentData.txt", 'w')
finally:
    file.close()

# 2.关闭系统前存储
file = open("studentData.txt", 'w')
# TypeError: write() argument must be str, not Student
file.write(xiaoming_str)
file.close()
