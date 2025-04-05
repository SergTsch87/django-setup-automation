def some_func_1(a: int, b: int):
    return a + b


def some_func_2():
    print('some text')


def main():
    some_func_2()
    print(some_func_1(4, 7))


if __name__ == '__main__':
    main()