# parent class
class car:

    # __init__ is known as the constructor
    def __init__(self,model,brand,color):
        self.model = model
        self.brand = brand
        self.color = color


    def start(self):
        print("start the car", self.model ,self.brand ,self.color)
    def move(self):
        print("move the car", self.model ,self.brand ,self.color)
    def stop(self):
        print("stop the car", self.model ,self.brand ,self.color)


c = car('x1','audi','white')
c.start()
c.move()
c.stop()

class BMW(car):
    def __init__(self, model, brand, color):
        super().__init__(model, brand, color)

    def autopilot(self):
        print("self driving the car", self.model ,self.brand ,self.color)
    def autogear(self):
        print("automating gear", self.model ,self.brand ,self.color)

b = BMW('z7','bmw','red')
b.start()
b.move()
b.stop()
b.autopilot()
b.autogear()
