class Employee:
    company = "Google"

class Freelancer:
    company = "Fiverr"

# class Programmer(Employee,Freelancer):
    pass
class Programmer(Freelancer,Employee):
    name = "XAJX"

p = Programmer()
print(p.company)