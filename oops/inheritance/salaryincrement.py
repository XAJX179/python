class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterment(self):
        return self.salary * self.increment

    @salaryAfterment.setter
    def salaryAfterment(self, sai):
        self.increment = sai/self.salary


xajx = Employee()
print(xajx.salary)
print(xajx.salaryAfterment)
xajx.salaryAfterment = 2500
print(xajx.salaryAfterment)
print(xajx.increment)