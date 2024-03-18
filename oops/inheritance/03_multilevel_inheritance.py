class Granpa:
    @staticmethod
    def breathe():
        print("I Am Breathing...")
class Parent(Granpa):
    pass
    # @staticmethod
    # def breathe():
        # print("I Am Breathing Snor Snor...")#Try playing these lines

class Child(Parent):
    pass
    # @staticmethod
    # def breathe():
        # print("I Am Breathing hehehehehehe...")#

g = Granpa()
g.breathe()
p = Parent()
p.breathe()
c = Child()
c.breathe()