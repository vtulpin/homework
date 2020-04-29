a= int(input("Введите выручку фирмы"))
b=int(input("Введите издержку фирмы"))
if a > b:
 print ('Прибыль')
 c = (a-b)/a
 d=int(input('Введите кол-во сотрудников'))
 e = c/d
 print (e)
elif a < b:
    print ('Убыток')