

file = input('Введите имя файла')
out_f = open(file, "w")
while True:
    f = input()
    if f == '':
        break
    out_f.write(f+'/n')
out_f.close()