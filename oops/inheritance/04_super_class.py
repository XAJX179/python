class Granpa:
    @staticmethod
    def breathe():
        print("I Am Breathing...")


class Parent(Granpa):
    @staticmethod
    def breathe():
        print("I Am Breathing Snor Snor...")  # Try playing these lines


class Child(Parent):
    @staticmethod
    def breathe():
        super(Parent,Child).breathe() #This is because of @staticmethod usage


g = Granpa()
g.breathe()

p = Parent()
p.breathe()

c = Child()
c.breathe()
