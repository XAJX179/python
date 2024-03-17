class Number:
    def _sum_func(self):
        return self.a+self.b

no1 = Number()
no1.a= 12
no1.b= 13

result=no1._sum_func()

print(result)