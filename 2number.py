
for line in open("file.txt", 'r'):
    lines += 1
    letters += len(line)
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
print("Строки", line)
print("Слова", Words)
print("Буквы", Letters)