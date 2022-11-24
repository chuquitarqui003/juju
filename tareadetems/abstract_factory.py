class Shop(object):
    def __init__(self,item_factory=None):
        self.item_factory=item_factory

    def get__item__description(self):
        item=self.item_factory.get_item()

        print("item model",self.item_factory.model())
        print("item name",item.name())
        print("item color",self.item_factory.color())


class Shoes(object):
    def name(self):
        return"Shoes"
    def __str__(self):
        return"Shoes"

class mobile(object):
    def name(self):
        return"nokia"
    def __str__(self):
        return"nokia"

class car(object):
    def name(self):
        return"toyota"
    def __str__(self):
        return"toyota"

class ShoesFactory(object):
    def get_item(self):
        return Shoes()
    def model(self):
        return"MEN101"
    def color(self):
        return"amarillo"

class carFactory(object):
    def get_item(self):
        return car()
    def model(self):
        return"camry"
    def color(self):
        return"rojo"

class mobileFactory(object):
    def get_item(self):
        return mobile()
    def model(self):
        return"nokia404"
    def color(self):
        return"azul"



shopShoes=Shop(ShoesFactory())
shopShoes.get__item__description()
print("*"*30)
shopmobile=Shop(mobileFactory())
shopmobile.get__item__description()
print("*"*30)
shopcar=Shop(carFactory())
shopcar.get__item__description()
