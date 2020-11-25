# <class 'dict'> {KEY:VALUE}
infors = {'Name': 'Alice Evans',
          'City': 'London',
          'Occupation': 'Manager'}
# print(type(infors))
# print(infors['Name'])
# print(infors)

# []取值再进行赋值时,已有key则修改,没有的key则新建
# infors['Age'] = 20
# print(infors[0]) KeyError: 0

# infors['Name'] = "xiaoming"
# print(infors)


# del关键字进行键值对的删除
# del infors['Age']
# print(infors)

dic_out = {}
print(dic_out)
print(type(dic_out))
dic_out['Alice'] = {'Name': 'Alice Evans', 'City': 'London', 'Age': 34}
dic_out['Jack'] = {'Name': 'Jack Edwood', 'City': 'Paris', 'Age': 24}
print(dic_out)
print(dic_out['Alice']['Name'])

