def myfunc(x, y):
    return 1 / x ** abs(y)


def myfunc1():
    print(myfunc(2, -2))


def myfunc2(x,y):
  r = 1
  for i in range(abs(y)):
        r = r * x
  return 1 /r
def myfunc2():
  print(myfunc2(2,-2))

