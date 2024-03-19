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
        for i in range(len(vec1.vec)):
            listy.append(vec1.vec[i]+vec2.vec[i])
        return Vector(listy) #print(Vector([11,44,66]))

    def __mul__(vec1,vec2):
        sum = 0
        for i in range(len(vec1.vec)):
            sum += vec1.vec[i] * vec2.vec[i]
        
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([1,4,6])
v2 = Vector([10,40,60])

print(v1)
print(len(v1))
print(len(v2))