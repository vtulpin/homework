from time import sleep


class Trafficlights:
    __color = ["Красный", "Желтый", "Зеленый"]

    def counter(self):
        i = 0
        while i !=3:
            print(Trafficlights.__color[i])
            sleep(7)
        elif i == 1:
            sleep(2)
        elif i == 2:
            sleep(4)


a = Trafficlights
a.counter()
