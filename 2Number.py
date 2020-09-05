number_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
a=[]
for i in range(len(number_list)-1):
    if number_list[i] < number_list[i+1]:
        a.append(number_list[i+1])
print (a)