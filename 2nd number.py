number = int(input ("Введите время в секундах"))
hours = number/3600
minutes = (number//60)
seconds = number%60
print (hours, minutes, seconds)