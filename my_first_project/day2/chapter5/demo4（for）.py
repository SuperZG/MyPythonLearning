# names = ['Alice', 'Bob', 'Dave', 'Mark', 'Jason']
# for name in names:
#     print('Hello!', name)

# <class 'range'>
# num_list = list(range(10))
# print(type(num_list))
# for num in num_list:
#     print(num)


# 思考下如何完成1~100的求和。
count = 0
num_list = list(range(1, 101))
# print(num_list)
for num in num_list:
    count += num

print("和为:", count)
