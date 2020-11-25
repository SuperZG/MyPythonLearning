# 排队软件:用已学知识实现饭店的取号和叫号功能
# 全局变量
num_list = []
count = 0


# 取号: 用什么数据结构存储我们客户去过号好呢?
#     1.不止一个
#     2.可变
#     3.先后顺序
def make_num():
    global count
    count = count + 1
    print("目前有%d个客人在排队" % len(num_list))
    print("您好,您取得的用餐号码为", count)
    num_list.append(count)


# 叫号: 从我们客户取号的列表中取号
def eat_num():
    # list 为空时,可以表示为False
    if num_list:
        eat_now = num_list.pop(0)
        print("请第%d号客人开始用餐" % eat_now)
        print("目前有%d个客人在排队" % len(num_list))
    else:
        print("目前没有排队的客人")


print("=" * 8 + "欢迎使用XXX饭店排队系统" + "=" * 8)
flag = True
while flag:
    print("=" * 30)
    req_num = input("请输入您的选项[1.取号;2.叫号]:")
    if req_num == '1':
        make_num()
    elif req_num == '2':
        eat_num()
    else:
        flag = False
        print("=" * 10 + "欢迎再次使用,再见!" + "=" * 10)