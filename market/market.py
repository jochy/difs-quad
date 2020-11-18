
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discount:
    def __init__(self, name, minQt, discount):
        self.name = name
        self.minQt = minQt
        self.discount = discount

class Cart:
    def __init__(self, prodList, discList):
        self.prodList = prodList
        self.discList = discList

'Now lets buy some products'

p1 = Product('Poulet', 2)
p2 = Product('Courgette', 0.2)
p3 = Product('Pomme de terre', 0.1)
p4 = Product('Champignon', 0.2)

d1 = Discount('Pomme de terre', 5, 0.1)
d2 = Discount('Poulet', 10, 4)
d3 = Discount('Courgette', 10, 1)

c = Cart({p1 : 2, p2 : 4, p3 : 6, p4 : 2}, [d1, d2])

'Now lets pay'
p = 0
for key in c.prodList:
    p = p + key.price * c.prodList[key]

    for d in c.discList:
        if key.name == d.name and c.prodList[key] > d.minQt:
            p = p - d.discount

'Now verify that this is the correct price'
expected =  4 + 0.8 + 0.6 + 0.4 - 0.1
if format(p, '.2f') != format(expected, '.2f'):
    raise RuntimeError('Something is wrong: got ' + str(p) + ' expected ' + str(expected))
else:
    print('Working')