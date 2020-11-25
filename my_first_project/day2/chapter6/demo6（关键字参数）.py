# 接收字典，需要放在必选参数后面
def infos(name, age, **others):
    print('\nName:', name, '\nAge:', age, '\nOther Info:', others)


# infos('Jack', 32)
# infos('Jason', 27, city='Beijing',region='dongbei')
extra = {'City': 'Shanghai', 'Job': 'HR', 'Gender': 'Male'}
# extra = {1,32,3}
# TypeError: infos() argument after ** must be a mapping, not set
infos('Bob', 31, **extra)
