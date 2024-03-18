class Employee:
    company= "Google"

    def showDetails(self):
        print("This Is An Employee")

class Programmer(Employee):
    lang= "Python"
    def getLang(self):
        print(f"Lang : {self.lang}")

xajx = Employee()
print(xajx.company)
xajx2 = Programmer()
print(xajx2.company)
xajx2.getLang()