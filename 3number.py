def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return sum(d)


def my_func2():
    print(my_func(4, 1, 9))