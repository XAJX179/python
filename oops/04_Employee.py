class Employee:
    company="Google"
    salary=1000000
xajx = Employee()
raj = Employee()
kaju = Employee()

xajx.company="Microsoft"
Employee.company="Youtube"

print(xajx.company)
print(raj.company)
print(kaju.company)

xajx.salary=12323
print(xajx.salary)
print(raj.salary)
print(kaju.salary)

