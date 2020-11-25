# 一. 导入模块两种方式

import makeinfos
first = makeinfos.infos('Tom', 'LA', 25)
print(first)

second = makeinfos.infos('xiaoming','beijing')
print(second)


# from makeinfos import infos
# second = infos('xiaoming','beijing')
# print(second)


# 二. 起别名 不提倡使用,不利于代码的阅读,不便于记忆.
# import makeinfos as mi
# third = mi.infos('xiaoming','beijing')
# print(third)

# from makeinfos import infos as ios
#
# forth = ios('xiaoming', 'beijing')
# print(forth)

# 三. 导入多函数
# 用*全部导入变量或函数的情况,不推荐
# 1.阅读不便
# 2.容易冲突
# from makeinfos import *

from makeinfos import make_num,eat_num
make_num()
eat_num()



