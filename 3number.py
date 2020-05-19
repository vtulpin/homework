class Worker:
    def __init__(self, name='Vasily',surname='Pupkin',position='manager',wage=100, bonus=100):
        self.name = name
        self.surname = surname
        self.position = position
        self.income={'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return self.name + self.surname
    def get_total_income(self):
        return self.income['bonus'] + self.income['wage']