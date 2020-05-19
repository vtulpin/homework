class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        if self.speed != 0:
            print('Едет')
    def stop(self):
        if self.speed == 0:
            print('Остановились')
    def turn(self, side):
        if side == 1:
            print('Поворачиваете влево')
        if side == 2:
            print('Поворачиваете вправо')