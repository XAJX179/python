class Vector:
    def __init__(self,vec):
        self.vec = vec
    
    def __str__(self) :
        str =''
        index = 0
        for i in self.vec:
            str += f" {i}a{index} +"
            index += 1
        return str[:-1]

    def __add__(vec1,vec2):
        listy = []
        if len(vec1.vec) == len(vec2.vec):
                
            for i in range(len(vec1.vec)):
                listy.append(vec1.vec[i]+vec2.vec[i])
            return Vector(listy) #print(Vector([11,44,66]))
        else:
            print("Length Are not same!")

    def __mul__(vec1,vec2):
        sum = 0
        if len(vec1.vec) == len(vec2.vec):
            for i in range(len(vec1.vec)):
                sum += vec1.vec[i] * vec2.vec[i]
            
            return sum
        else:
             print("Length Are not same!")


v1 = Vector([1,4,6])
v2 = Vector([10,40,60])

print(v1)
print(v1+v2)
print(v1*v2)