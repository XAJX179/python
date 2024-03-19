class Complex:
    def __init__(self,r,i) :
        self.real = r
        self.imaginary = i

    def __str__(self) :
        return  f"{self.real} {self.imaginary}i"

    def __add__(a,b):
        return Complex(a.real+b.real,a.imaginary+b.imaginary)

    def __mul__(x,y):
        mulR = x.real * y.real - x.imaginary * y.imaginary
        mulI = x.real * y.imaginary + x.imaginary * y.real
        return Complex(mulR,mulI)

c1= Complex(3,2)
c2= Complex(1,7)

print(c1+c2)
print(c1*c2)