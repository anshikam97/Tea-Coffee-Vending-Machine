from TCVM import Container, refillandreset
from time import sleep


class machine:
    choice = 0
    ord = []

    def __init__(self):
        while True:
            self.printO()

            if machine.choice == 1:
                self.make()

            elif machine.choice == 2:
                a = refillandreset.r()
                a.refill()
                machine.ord = []
                refillandreset.r.ts = []

            elif machine.choice == 3:
                a = refillandreset.r()
                a.stats()

            elif machine.choice == 4:
                a = refillandreset.r()
                a.refill()

            elif machine.choice == 5:
                self.orderlist()

            elif machine.choice == 6:
                a = refillandreset.r()
                a.totalsale()

            elif machine.choice == 7:
                break

    def printO(self):
        print("-------------------")
        print("1. Order")
        print("2. Reset Machine")
        print("3. Container Status")
        print("4. Refill Container")
        print("5. Order list")
        print("6. Total amount collected")
        print("7. Exit")
        machine.choice = int(input("Enter your Choice: "))

    def make(self):
        self.box()
        i = input("Your Order: ")
        data = i.split(" ")
        v = []

        for i in range(0, len(data) - 1, 2):
            if i % 2 == 0:
                v.append([int(data[i]), str(data[i + 1])])

        for i in v:

            if i[1] == "tea" or i[1] == "t":
                b = Container.underflow()
                b.underfw(i[0])
                if b.uf == False:
                    machine.ord.append("{} {}".format(i[0], i[1]))
                    c = Container.usage()
                    c.tea(i[0])

            if i[1] == "coffee" or i[1] == "c":
                b = Container.underflow()
                b.underfw(i[0])
                if b.uf == False:
                    machine.ord.append("{} {}".format(i[0], i[1]))
                    c = Container.usage()
                    c.coffee(i[0])

            if i[1] == "blacktea" or i[1] == "bt":
                b = Container.underflow()
                b.underfw(i[0])
                if b.uf == False:
                    machine.ord.append("{} {}".format(i[0], i[1]))
                    c = Container.usage()
                    c.blacktea(i[0])

            if i[1] == "blackcoffee" or i[1] == "ct":
                b = Container.underflow()
                b.underfw(i[0])
                if b.uf == False:
                    machine.ord.append("{} {}".format(i[0], i[1]))
                    c = Container.usage()
                    c.blackcoffee(i[0])

        self.suc()

    def orderlist(self):
        for i in machine.ord:
            print(i)

    def box(self):
        sleep(0.3)
        print("__________________________________________")
        print("------------------------------------------")
        print("|       |        |          |             |")
        print("|  TEA  | COFFEE | BLACKTEA | BLACKCOFFEE |")
        print("|  (t)  |   (c)  |   (bt)   |     (bc)    |")
        print("__________________________________________")
        print("----_-------_---------_-----------_-------")

    def suc(self):
        sleep(1)
        print("order taken successfully")
        sleep(2)
        print("processing now ")
        for i in range(1, 10):
            print(i * ".")
            sleep(0.5)
        print("Your order is ready")
        a = refillandreset.r()
        a.sale()
        a.resetprice()


machine()
