# Exam
# سوال یک

class equilateral():
    def mohit(self, side):
        # محیط = یک ضلع × ۳ و تقسیم بر ۲
        
        self.side = side
        mohit = (side * 3) / 2
        print(mohit)
        
    def masahat(self, rule, height):
        # مساحت = قاعده × ارتفاع
        
        self.rule = rule
        self.height = height
        masahat = rule * height
        print(masahat)
      
        
sample = equilateral()
sample.mohit(20)
sample.masahat(15, 10)