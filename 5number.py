numbers= input('Введите числа через пробел')
file= open ('numbers.txt', "w")
file.write(numbers)
numbers=numbers.split()
sum_numbers=0
for number in numbers:
    try:
        sum_numbers +=int(number)
    except ValueError:
        continue
 print(sum_numbers)
 file.close()