# print(dir(object))
# class A:
#     """
    
#     """

class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(f"i'm a Cat, named {self.name}, age {self.age}")


    def make_sound(self):
        print('Meow')

class Dog:
    def __init__(self, name , age) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(f"i'm a Dog, named {self.name}, age {self.age}")  

    def make_sound(self):
        print('Meow') 
