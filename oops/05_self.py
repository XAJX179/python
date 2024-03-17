class Employee:
    company= "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

xajx = Employee()
xajx.salary=100500
Employee.getSalary(xajx) #this argument is why it requires 'self' above in getSalary
xajx.getSalary() # short way to write it