# Exam
# سوال دو

class square:
    def __init__(self, side, diameter):
        self.side = side
        self.diameter = diameter
        
    def masahat(self):
        masahat = self.side * self.side
        print(masahat)
        
class diamond(square):
    def __init__(self, smallDiameter):
        super().__init__(self)
        self.smallDiameter = smallDiameter
        # self.bigDiameter = bigDiameter
        
    def masahat(self):
        masahat = (self.diameter * self.smallDiameter) / 2
        print(masahat)
        

        
sample_sq = square(20, 15)
sample_sq.masahat()

sample_di = diamond(10)
sample_di.masahat()