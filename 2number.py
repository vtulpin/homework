class OwnError(Exception):
    def __init__(self, number):
        self.number = number

dat = input ("Введите число")
try:
     dat = int(dat)
     if dat == 0:
         print("Результат деления = 0")
except ValueError:
    print("Вы не ввели число")
else:
    if dat > 0:
        print("Результат деления тоже равен нулю")
