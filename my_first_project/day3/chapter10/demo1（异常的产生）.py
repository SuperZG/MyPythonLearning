if __name__ == '__main__':
    while True:
        try:
            a = int(input("请输入一个数字"))
            print(10 / a)
            #     ZeroDivisionError: division by zero

        # except 预先判定异常的类型,如果满足,则执行下面的代码
        except ZeroDivisionError:
            print("你打印的是0吧")

        except ValueError:
            print("你打印的是字符串吧")
        # 当没有异常时再执行else
        else:
            print("好的,收到")
        # finally 后面是一定可以执行的代码,无论有没有异常,而且即使异常没有预判到
        finally:
            print("欢迎再次使用")

