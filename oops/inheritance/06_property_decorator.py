class Employee:
    company = "TCS"
    salary = 4600
    salaryBonus = 500
    # totalSalary = 5100

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salary = val - self.salaryBonus #assuming Bonus stays constant



e = Employee()
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)

e.totalSalary= 5000
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)
