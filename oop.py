# class Perse:
#     def show(self, name = 'Unknown'):
#         print('hello' + name)

# x = Perse()
# y = Perse()
# x.show()
# y.show('alise')




# class Perse:

#     def __init__(self, valuta, name='Unknown'):
#         self.money = 0.00
#         self.valuta = valuta
#         self.name = name


#     def top_up_balance(self, howmany):
#         self.money = self.money + howmany


#     def top_down_balance(self, howmany):
#         if self.money - self.money < 0:
#             print('ne dostatochno sredstv')
#             raise ValueError ('ne dostatichno sredstv')
#         self.money = self.money - howmany

#     def info(self):
#         print(self.money)


#     def __del__(self):
#         print('cash dalated')
        




# x = Perse('USD')
# y = Perse('EUR','Bill' )
# x.top_up_balance(100)
# x.info()



"""""vidos Kani"""

# def decorator(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошел успешно')
#     return wrapper

# @decorator
# def first():
#     print("I'm a func")
# first()


# 1

# def call_function(func):
#     name = func.__name__
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func()
#         print(f"Вызов функции {func.__name__} прошёл успешно")
#     return wrapper
# @call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()


# 2


# class Circle:
#     color = "Синий"
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return Circle.pi*self.radius**2


# circle = Circle(2)
# circle.color = "red"
# circle.get_area()

# 3

# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")

# contact = Phone("John", "Snow", +996707707707)
# contact.get_info()

# 4

# class Dog:
#     def voice(self):
#         return 'Гав'
# class Cat:
#     def voice(self):
#         return "Мяу"

# barsik = Cat()
# rex = Dog()

# def to_pet(x):
#     if x == barsik:
#         return barsik.voice()
#     return rex.voice()

# print(to_pet(barsik)) 
# print(to_pet(rex))

# 5

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')

# person = Person('anton',18)
# student = Student('anton', 18, 'phizic')
# student.display_student()
# person.display()

# print(student.name,student.age,student.faculty)


# class Circle:
#     color = "Синий"
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         print(Circle.pi*self.radius**2)


# circle = Circle(2)
# circle.color = "red"
# circle.get_area()
    

# class Phon:
#     def __init__(self, first_name, last_name,num) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.num = num

#     def get_info(self):
#         print(f"Контакт: {self.first_name} {self.last_name}, телефон: {self.num}")

# contact = Phon('Ivan', 'Petrov', +996555777888)
# contact.get_info()


# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")

# contact = Phone("John", "Snow", +996707707707)
# contact.get_info()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')

# student = Person('Aidana', 19)
# student = Student('Aidana',  19 ,'Python')
# student.display_student()
# student.display()

# print(student.name,student.age,student.faculty)


# class Person:
#     def __init__(self,name, age) -> None:
#         self.name = name 
#         self.age = age

#     def display(self):
#         print(f"Imya: {self.name}, Vozrast {self.age}")

# class Student(Person):
#     def __init__(self, name, age, fukulti) -> None:
#         super().__init__(name, age)
#         self.fukulti = fukulti

#     def display_student(self):
#         print(f"Imya: {self.name}, Vozrast: {self.age},Fucultet: {self.fukulti}")


# studnt = Person("Aidana",19)
# studnt = Student("Aidana",19, "Python")
# studnt.display()
# studnt.display_student()

# class Dog:
    

# class Cat:


# class Dog:
#     def voice(self):
#         return 'Гав'

# class Cat:
#     def voice(self):
#         return "Мяу"

# dazai = Cat()
# oda = Dog()

# def to_pet(x):
#     if x == dazai:
#         return dazai.voice()
#     return oda.voice()

# print(to_pet(dazai)) 
# print(to_pet(oda))






