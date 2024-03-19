class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):

    @staticmethod
    def bark():
        print("Bhow Bhow!")

tommy = Dog()
tommy.bark()