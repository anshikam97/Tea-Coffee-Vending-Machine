from TCVM import Container as cn


class r:

    ts = []

    def refill(self):
        cn.container.teaC = 2000
        cn.container.coffeeC = 2000
        cn.container.sugarC = 8000
        cn.container.sugarC = 8000
        cn.container.milkC = 10000

    # def reset(self):
    #     cn.container.teaC = 2000
    #     cn.container.coffeeC = 2000
    #     cn.container.sugarC = 8000
    #     cn.container.sugarC = 8000
    #     cn.container.milkC = 10000
    #     cn.usage.price = 0

    def sale(self):
        print("total amount is: ",cn.usage.price)
        r.ts.append(cn.usage.price)

    def totalsale(self):
        print("total sale is: ", sum(r.ts))

    def stats(self):
        print("tea",cn.container.teaC)
        print("coffee",cn.container.coffeeC)
        print("milk",cn.container.milkC)
        print("sugar",cn.container.sugarC)
        print("water",cn.container.waterC)

    def resetprice(self):
        cn.usage.price = 0