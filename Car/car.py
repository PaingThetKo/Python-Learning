class Car :
    sterringwheel=1 #cls lvl attribute
    def __init__(self,name,wheels):  #instance lvl attribute
        self.name = name
        self.wheels = wheels

    def drive(self):
        print(f'{self.name} is driving with {self.wheels} wheels.')

    @classmethod
    def common(cls):
        print(f'all cars have only {cls.sterringwheel} sterringwheel.')

bmw = Car ("BMW M2",4)
bmw.common()

# bmw = Car ("BMW M2",4)
# bmw.drive()

# audi = Car ("AUDI TT", 4)
# audi.drive() 