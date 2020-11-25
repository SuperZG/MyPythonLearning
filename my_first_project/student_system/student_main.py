from student_system.studentClass import Student

student_list = []
count = 0


# 1.查询所有学生
def searchAll():
    for student in student_list:
        print(student)


# 2.查询学生信息
def searchOne():
    student_id = input("请输入要查询的学生id:")
    for student in student_list:
        if str(student.id) == student_id:
            print(student)
            return
    else:
        print("该学生id不存在")


# 3.添加学生
def addOne():
    global count
    student_id = count
    student_name = input("请输入学生姓名:")
    student_gender = input("请输入学生性别:")
    student_tel = input("请输入学生电话:")
    student = Student(student_id, student_name, student_gender, student_tel)
    student_list.append(student)
    count = count + 1


# 4.修改学生
def updateOne():
    searchAll()
    student_id = input("请输入要修改的学生id:")
    for student in student_list:
        if str(student.id) == student_id:
            student_gender = input("请输入学生性别:")
            student_tel = input("请输入学生电话:")
            student.gender = student_gender
            student.tel = student_tel
            print("%s号学生修改成功!" % student_id)
            return
    else:
        print("该学生id不存在")


# 5.删除学生
def deleteOne():
    student_id = input("请输入要修改的学生id:")
    # for i in range(len(student_list)):
    #     # student_list[i] 表示我们列表的第i个索引位的学生对象
    #     if str(student_list[i].id) == student_id:
    #         # del student_list[i]
    #         student_list.pop(i)
    #         print("%s号学生删除成功!" % student_id)
    #         return
    for student in student_list:
        if str(student.id) == student_id:
            student_list.remove(student)
            print("%s号学生删除成功!" % student_id)
            return
    else:
        print("该学生id不存在")


def main():
    flag = True
    while flag:
        # (1)显示系统信息
        print("+" * 22)
        print("欢迎使用学生管理系统")
        print("+" * 22)
        print("1.查询所有学生")
        print("2.查询学生信息")
        print("3.添加学生")
        print("4.修改学生")
        print("5.删除学生")
        print("0.退出系统")
        # (2)接收用户输入的信息
        todo = input("请输入您需要输入的操作(例如:1):")
        # (3)判断并执行用户的需求
        if todo == '1':
            searchAll()
        elif todo == '2':
            searchOne()
        elif todo == '3':
            addOne()
        elif todo == '4':
            updateOne()
        elif todo == '5':
            deleteOne()
        else:
            flag = False
            print("感谢您的使用.")


if __name__ == '__main__':
    main()