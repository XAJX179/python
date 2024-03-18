class Employee:
    company = "Google"

class Freelancer:
    company = "Fiverr"

# class Programmer(Employee,Freelancer):

class Programmer(Employee,Freelancer):
    name = "XAJX"

p = Programmer()
print(p.company)