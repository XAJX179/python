class Employee:
    Company = "Google Inc"

    def __init__(self,salary,name,unit):
        self.greet()
        self.salary = salary
        self.name = name
        self.unit = unit

    @staticmethod
    def greet():
        print("Good Morning!!!")

    def printDetails(self):
        print(f'''Name : {self.name}
Salary : {self.salary}
Company : {self.Company}
Unit : {self.unit}        
''')


xajx = Employee(100,"xajx","Yt")
xajx.printDetails()

raj = Employee(100,"raj","Google")
raj.printDetails()

kaju = Employee(100,"kaju","Maps")
kaju.printDetails()
