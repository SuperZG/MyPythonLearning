# 思考下如何完成1~100的求和。
# 1.range+for
# count = 0
# num_list = list(range(0, 101,2))
# print(num_list)
# for num in num_list:
#     count += num
# print("和为:", count)

# 2.for+if
# count = 0
# num_list = list(range(0, 101))
# print(num_list)
# for num in num_list:
#     if num % 2 == 0:
#         count += num
#
# print("和为:", count)

# 3.for+continue
# count = 0
# num_list = list(range(0, 101))
# print(num_list)
# for num in num_list:
#     if num % 2 == 1:
#         continue
#     count += num
#
# print("和为:", count)

# 4.while+if
# sum = 0
# x = 0
# while x <= 100:
#     if x%2==0:
#         sum = sum + x
#     x = x + 1
# print(sum)

# 5.while+continue
# sum = 0
# x = 0
# while x <= 100:
#     x = x + 1
#     if x % 2 == 1:
#         continue
#     sum = sum + x
# print(sum)

# 6.while+range
num_list = list(range(0, 101, 2))
print(num_list)
# 求list的长度
# print(len(num_list))
# print(num_list.__len__())

# list[index]
sum = 0
x = 0
while x < len(num_list):
    sum = sum + num_list[x]
    x = x + 1
print(sum)
