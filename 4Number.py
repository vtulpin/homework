f1 = open('text_4.txt')
f1.readlines()
l=["Один","Два","Три","Четыре"]
f2 = open('newdata.txt', 'w')
f2.writelines("%s/n" % line for line in l)