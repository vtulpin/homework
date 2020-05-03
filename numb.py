my_list = [7, 5, 3, 3, 2]
print(f'список {my_list}')
my_list.append(int(input('Введите цифру: ')))
print(f'теперь список:{sorted(my_list, reverse=True)}')
# пятый номер