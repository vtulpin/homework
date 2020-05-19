import time 


def running(color):
    for i in range(len(color)):
        print(i)
        if i == 0:
            print(color[i])
            time.sleep(7)
        elif i == 1:
            print(color[i])
            time.sleep(2)
        else:
            print(color[i])
            time.sleep(10)


color = ["red", "yellow", "green"]

running(color)