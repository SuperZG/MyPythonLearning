'''
此模块是一个模块
'''


def infos(name, city, age=''):
    '''
    此方法是一个方法
    :param name:
    :param city:
    :param age:
    :return: people_info
    '''
    people_info = {'name': name, 'city': city}
    # age 为空则不执行
    if age:
        people_info['age'] = age
    return people_info


def make_num():
    print("您好,您取得的用餐号码为")


# 叫号: 从我们客户取号的列表中取号
def eat_num():
    # list 为空时,可以表示为False
    print("目前没有排队的客人")


count = 0




