import json
from studentClassDemo import Student


def object2dict(student):
    return {"id": student.id, "name": student.name, "gender": student.gender, "tel": student.tel}


def dict2object(dict):
    return Student(dict['id'], dict['name'], dict['gender'], dict['tel'])


if __name__ == '__main__':
    xiaoming = Student(1, "小明", "男", "13333333333")
    # Object of type Student is not JSON serializable
    # json_str = json.dumps(xiaoming)
    # print(json_str)

    student_dict = object2dict(xiaoming)
    print(student_dict)
    print(type(student_dict))

    XiaoMing = dict2object(student_dict)
    print(XiaoMing)
    print(type(XiaoMing))
