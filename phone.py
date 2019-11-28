class phone:
    def __init__(self, brandName, size):
        self.brand =  brandName
        self.screen = size
    def showSize(self):
        print(self.screen)
    def showBrand(self):
        print(self.brand)
