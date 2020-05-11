from itertools import cycle
a=0
for i in cycle('abc'):
    if a > 30:
        break
    else:
        print(i)
        a +=1