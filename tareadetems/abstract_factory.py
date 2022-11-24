class Shop(object):
    def __init__(self,item_factory=None):
        self.item_factory=item_factory

    def get__item__description(self):
        item=self.item_factory.get_item()

        print("modelo del articulo",self.item_factory.model())
        print("nombre del articulo",item.name())
        print("color del articulo",self.item_factory.color())


class Shoes(object):
    def name(self):
        return"zapatos"
    def __str__(self):
        return"zapatos"

class mobile(object):
    def name(self):
        return"celular"
    def __str__(self):
        return"celular"

class car(object):
    def name(self):
        return"carro"
    def __str__(self):
        return"carro"

class ShoesFactory(object):
    def get_item(self):
        return Shoes()
    def model(self):
        return"MEN101"
    def color(self):
        return"negro"

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
