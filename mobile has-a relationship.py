# parent class
class memory:

    # __init__ is known as the constructor
    def __init__(self, internal, secondary, ram):
        self.internal = internal
        self.secondary = secondary
        self.ram = ram

    def config(self):
        print('memory features:', self.internal, self.secondary, self.ram)


class mobile:

    def __init__(self, model, brand, price, internal, secondary, ram):
        self.model = model
        self.brand = brand
        self.price = price
        self.obj_memory = memory(internal, secondary, ram)

    def display(self):
        self.obj_memory.config()
        print("mobile config:", self.model, self.brand, self.price, self.obj_memory)


m2 = mobile('on6', 'samsung', '6500', '32', '64', '4')
m2.display()
