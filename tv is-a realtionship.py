# parent class
class tv:

    # __init__ is known as the constructor
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand


    def features(self):
        print("tv features:", self.model ,self.brand )


t = tv('bravio', 'sony')
t.features()

class smarttv(tv):
    def __init__(self, model, brand, screensize, price,resolution):
        super().__init__(model, brand)
        self.screensize = screensize
        self.price = price
        self.resolution = resolution

    def newfeatures(self):
        print("smarttv added new features:", self.model, self.brand, self.screensize, self.price, self.resolution)

t = smarttv('thunder', 'samsung', '43', '50000', '1080')
t.newfeatures()