class Employee:
    country = "Japan"

    @classmethod
    def changeCountry(cls,countryName):
        cls.country = countryName

print(Employee.country)
p1 = Employee()
p1.changeCountry("China")
print(Employee.country)
