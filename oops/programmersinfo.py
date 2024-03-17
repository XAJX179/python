class Programmer:
    def __init__(self,name,lang,end):
        self.name = name
        self.language = lang
        self.BacKOrFrontEnd = end

    def getInfo(self):
        print(f'''Name : {self.name}
Language : {self.language}
Speciality : {self.BacKOrFrontEnd}
''')


xajx = Programmer("xajx","C","Back")
raj = Programmer("raj","js","Front")
kaju = Programmer("kaju","python","Back")


xajx.getInfo()
raj.getInfo()
kaju.getInfo()
