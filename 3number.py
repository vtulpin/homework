number_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [el for el in number_list if number_list.count(el) == 1]
print(my_list)
