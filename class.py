class Car :
    def __init__(self,name,wheels):
        self.name = name
        self.wheels = wheels

    def drive(self):
        print(f'{self.name} is driving with {self.wheels} wheels.')

bmw = Car ("BMW M2",4)
bmw.drive()

audi = Car ("AUDI TT", 4)
audi.drive()