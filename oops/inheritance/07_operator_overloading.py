class Number:
    def __init__(self,num) :
        self.num = num
    def __add__(self,num2):
        print(f"Add = {self.num+num2.num}")
    
    def __mul__(self,numbertwo):
        print(f"Multiply = {self.num*numbertwo.num}")

n1= Number(4)
n2= Number(6)
n1 + n2
n1 * n2