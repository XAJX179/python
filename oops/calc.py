class Number:
    def __init__(self,num):
        self.number=num
        self.cube()
        self.square()
     

    def square(self):
        print(f"Square : {self.number ** 2}")
    def cube(self):    
        print(f"Cube : {self.number ** 3}")
    def sqroot(self): 
        print(f"Sqroot : {self.number ** 0.5}")


num1 = Number(16)
num1.sqroot()