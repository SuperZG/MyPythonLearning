

if __name__ == '__main__':
    try:
        with open('D:\\inout9\\text2', 'r') as example:
            print(example.read(5))

    except Exception:
        print("您的路径应该是错的")
    finally:
        print("哈哈哈哈")
