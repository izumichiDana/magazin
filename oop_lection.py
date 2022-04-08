# # OOP ->  обьектно ориентированное программирование 

# class Person:
#     legs = 2
#     arms = 2
#     eyes = 2
#     mouth = 1
    
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         self.__secret = 'secret'
    
#     def walk(self, km):
#         print(f'{self.name} hodit {km} km')

# person1 = Person('Aidana', 18)
# person2 = Person('erma',18)



# print(person1)
# # print(person1._age)
# # print(person1._Person__secret)

# # person1.walk(3)

# OOP paradigma


# class Person:
#     def __init__(self, name, age, sex) -> None:
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.is_run = False
#         self.is_go = False
#         self.is_speak = False

#     def speak(self):
#         if self.age >5:
#             self.is_speak = True 
#         if self.is_speak:
#             print("speak successfuly")
#         else:
#             print("i can't speak")

#     def go(self):
#         if self.age >5:
#             self.is_go = True 
#         if self.is_go:
#             print("go successfuly")
#         else:
#             print("i can't go")

#     def run(self):
#         if self.age >5:
#             self.is_run = True 
#         if self.is_run:
#             print("run successfuly")
#         else:
#             print("i can't run")

# jhon = Person("jhon", age=5.1, sex='male')
# jhon.speak()
# jhon.run() 
# jhon.go()


"""                                              razbor                                                  """

# class Student:
#     def __init__(self, first_name , last_name) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.book = []
#         self.knowlage = 0
#         self.is_ready_to_work = False
#         self.languages = {}

#     def read_book(self, book_title):
#         self.book.append(book_title)
#         self.__add_points(100)

#     def do_home_work(self):
#         self.__add_points(10)

#     def do_real_world_project(self):
#         self.__add_points(50)

#     def __add_points(self, point):
#         self.knowlage += point
#         if self.knowlage >= 500:
#             print('This student is ready to work')
#             self.is_ready_to_work = True

#     def lern_new_language(self, name_of_language, num):
#         if num <1 or num >100:
#             raise ValueError("Invalid number")
#         self.languages[name_of_language] = num


# st1 = Student('Jhon', 'Connor')
# print(f'bally u {st1.first_name}:',st1.knowlage)
# st1.read_book('Terminator2')
# st1.read_book('Terminator3')
# st1.read_book('Terminator4')
# st1.read_book('Terminator5')
# st1.do_home_work()
# st1.do_real_world_project()
# st1.do_real_world_project()
# st1.lern_new_language("pithon", 10)
# st1.lern_new_language('JS', 10)
# print(f'bally u {st1.first_name}:',st1.knowlage)
# print(st1.languages)
# print(st1.book)



#  __init__ - inicializator

# creatrte read update delate


"""""                                       Base class должен быть продуман 
                                                Нужно учитывать логику                        """



# class BaseCrud:
#     def __init__(self) -> None:
#         self.data = []    
#         self.id_ = 1


#     def get(self, num_id):
#         for d in self.data:
#             if d.get(num_id):
#                 return d
#             else:
#                 return None

#     def create(self, data: dict):
#         self.data.append({self.id_ : data})
#         self.id_ += 1

#     def update(self, num_id, data : dict):
#         pass

#     def delate(self, num_id):
#         for d in self.data:
#             if d[num_id]:
#                 self.data.remove(d)

# class Book(BaseCrud):
#     pass

# book = Book()
# print("Befor call methodt create")
# book.create({"name": "python"})
# book.create({"name": "JS"})
# print("After call methodt create: ", book.data)
# print( "Searched", book.get(1))


# # 1 :'Some book'
# # 2 : 'some book'


# class Spam:
#     val = 1
#     def __init__(self, n) -> None:
#         val = 5


# obj = Spam(5)
# print(obj.val)


# from tkinter import Pack


# class Perent():
#     x =1 
#     y = 2 

# class Child(Perent):
#     x = 111
#     y = 222

#     def mix(self):
#         return Pack.y

# c = Child()
# print(c.mix())





#  наследование 
# инкапсуляция - пртватнфые и публичные методы или атртибуты 
# инкапсуляция - обьудинение в единое целое атрибутов и методов   


# class A():
#     a = 12 
#     def __init__(self) -> None:
#         self.hello = 'hello'

#     def set(self):
#         print('set')


# _ - защищенный 
# __ - приватный



# class BaseTest:

#     def equal(self,a,b):
#         return a == b


# class Test(BaseTest):
#     pass 

# test = Test()
# print(dir(test))



# class A:
#     def __init__(self):
#         self.a = 0

#     def change(self, n):
#         a = n

# obj = A()
# obj.change(2)
# print(obj.a)


# class Smap:
#     val = 1
#     def __init__(self, n) -> None:
#         val = 5

# o = Smap(5)
# print(o.val)


# class Parent():
#     x = 1 
#     y = 2

# class Child(Parent):
#     x = 111
#     y = 222

#     def mix(self):
#         return Parent.y

# c = Child()
# print(c.mix())


# class Num:
#     def __init__(self, num):
#         self.num = num
#         print(f'1000-{self.num}')

# Num('7')