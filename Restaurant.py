class RestaurnatTable:
    menu={
        'pizza': 10000,
        'cola' : 1000,
        'apple juice' : 2000,
        'hamburger' : 4500,
        'fried potato' : 1500
    }

    def __init__(self) :
        self.total=0
        self.orders=[]

    def addOrder(self,order):
        self.orders.append(order)
        self.total+=self.menu[order]

    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menu[order]}')

        print(f'total price is - {self.total}')


def startProgram():
    table=RestaurnatTable()

    while True :
        order = input('order : ')
        table.addOrder(order)

        another = input('would you like to add more ?  y/n : ')

        if another == 'y' :
            continue
        if another == 'n' :
            table.printBill()
            break

startProgram()