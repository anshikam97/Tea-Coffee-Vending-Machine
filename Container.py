class container:
    teaC = 2000
    coffeeC = 2000
    sugarC = 8000
    waterC = 15000
    milkC = 10000


class usage:
    teaU = 5
    bteaU = 3

    coffeeU = 4
    bcoffeeU = 3

    twaterU = 60
    bwaterU = 100
    cwaterU = 20

    tmilkU = 40
    cmilkU = 80

    sugarU = 15

    price = 0

    def coffee(self, quan):
        self.quan = quan
        container.coffeeC -= (usage.coffeeU * quan)
        container.sugarC -= (usage.sugarU * quan)
        container.waterC -= (usage.cwaterU * quan)
        container.milkC -= (usage.cmilkU * quan)
        usage.price += (15 * quan)

    def tea(self, quan):
        self.quan = quan
        container.teaC -= (usage.teaU * quan)
        container.sugarC -= (usage.sugarU * quan)
        container.waterC -= (usage.twaterU * quan)
        container.milkC -= (usage.tmilkU * quan)
        usage.price += (10 * quan)


    def blackcoffee(self, quan):
        self.quan = quan
        container.coffeeC -= (usage.bcoffeeU * quan)
        container.sugarC -= (usage.sugarU * quan)
        container.waterC -= (usage.bwaterU * quan)
        usage.price += (10 * quan)

    def blacktea(self, quan):
        self.quan = quan
        container.teaC -= (usage.bteaU * quan)
        container.sugarC -= (usage.sugarU * quan)
        container.waterC -= (usage.bwaterU * quan)
        usage.price += (5 * quan)


class underflow():

    uf = False

    def underfw(self, quan):

        self.quan = quan

        if container.teaC < quan*usage.teaU or container.teaC < quan*usage.bteaU:
            print("tea container is underflow")
            underflow.uf = True
        elif container.coffeeC < quan*usage.coffeeU or container.coffeeC < quan*usage.bcoffeeU:
            print("coffee container is underflow")
            underflow.uf = True
        elif container.sugarC < quan*usage.sugarU:
            print("sugar container is underflow")
            underflow.uf = True
        elif container.waterC < quan*usage.twaterU or container.waterC < quan*usage.bwaterU or container.waterC < quan*usage.cwaterU:
            print("water container is underflow")
            underflow.uf = True
        elif container.milkC < quan*usage.tmilkU or container.milkC < quan*usage.cmilkU:
            print("milk container is underflow")
            underflow.uf = True
        else:
            underflow.uf = False