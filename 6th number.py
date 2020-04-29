a = int(input('Введите результат 1 дня'))
b = int(input("Введите наименьшее кол-во км"))
day = 1
while  b-a > 0:
    a = a + (a*0.1)
    day +=1
print (day)