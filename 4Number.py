from functools import reduce
numbers=range(100,1000)
sum=reduce(lambda x, y: x + y, numbers)
print(sum)