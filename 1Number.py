def salary():
    x = int(input('Введите количество отработанных часов'))
    y = int(input('Введите суммы оплаты труда за 1 час'))
    z = int(input('Укажите размер премии'))
    g = x * y
    return g + z
print(f"Размер заработной платы составил {salary()}")