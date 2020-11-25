import json
from student_system2.studentClass import Student

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


def object2dict(student):
    return {"id": student.id, "name": student.name, "gender": student.gender, "tel": student.tel}


def dict2object(dict):
    return Student(dict['id'], dict['name'], dict['gender'], dict['tel'])


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
    try:
        # 1.打开系统先读取
        file = open("studentData.txt")
        # 读取文件内的字符串
        student_file_str = file.read()
        # 如果读取的字符串不为空,则执行
        if student_file_str != '':
            # 先将字符串转换为数据结构,使用loads方法
            student_dict_list = json.loads(student_file_str)
            # 使用for循环,将每一个dict转化为student,并添加到全局list中
            for student_dict in student_dict_list:
                student = dict2object(student_dict)
                student_list.append(student)
            # 在转换为对象后,将最后一个对象的id取出,加1后赋值给全局count
            student = student_list[-1]
            count = student.id + 1
    # 如果第一次运行程序,文件没找到,则用mode为w的方式新建一个文件
    except FileNotFoundError:
        file = open("studentData.txt", 'w')
    finally:
        # 关闭文件对象
        file.close()

    main()

    # 2.关闭系统前存储
    # 执行完main语句后,实现存储
    student_dict_list = []
    # 如果全局对象list为空,则不需要遍历
    if student_list:
        # 如果全局对象list不为空,则将每一个对象转换成一个dict
        for student in student_list:
            student_dict = object2dict(student)
            # 使用局部变量student_dict_list 存储我们的dict
            student_dict_list.append(student_dict)

    # 将我们的dict列表转换为json字符串
    student_list_str = json.dumps(student_dict_list)

    # 创建写方式的文件对象
    file = open("studentData.txt", 'w')
    # TypeError: write() argument must be str, not Student
    # 写入json字符串
    file.write(student_list_str)
    # 关闭文件对象
    file.close()
