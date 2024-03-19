class C2D:
    def __init__(self,i ,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f'''{self.icap}i + {self.jcap}j'''

class C3D(C2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k
    
    def __str__(self):
        return super().__str__() + f"+ {self.kcap}k"

a1 = C2D(2,5)
a2 = C3D(6,9,8)

print(a1)
print(a2)

