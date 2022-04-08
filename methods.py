# class A:
#     a = 'Class Var'
#     def __init__(self) -> None:
#         self.b = 'instance Var'

# print(A().b)


# class SomeClass:
#     def __init__(self,a , b) -> None:
#         self.a = a 
#         self.b = b
        
#     def func(self):
#         self.a = 10

#     @classmethod
#     def fonc_two(cls):
#         pass

#     @staticmethod
#     def func_three():
#         pass



# DELIVERY_PRICE = 120
# class Order:
#     orders = []
    
    
#     def __init__(self, name , adrees, product,price, count) -> None:
#         self.name = name 
#         self.adrees = adrees
#         self.product = product
#         self.price = price
#         self.count = count

#     def create_order(self):
#         order = {'name':self.name,
#                 'adrees':self.adrees,
#                 'product':self.product,
#                 'price':self.price,
#                 'count':self.count,
#                 'delivery':self.set_delivery(self.count, DELIVERY_PRICE)
#                 }
#         self.orders.append(order)

#     @staticmethod
#     def set_delivery(count, price):
#             return (price * count ) / 2

# order1 = Order("John", "California", "ice-cream", 250, 5)
# order2 = Order("Raychel", "LA", "ice-cream", 250, 10)
# order1.create_order()
# print(order1.orders)
# order2.create_order()
# print(order2.orders)
# print(Order.orders)


# class Pizza:

#     def __init__(self, name, radius, *ingredients) -> None:
#         self.name = name 
#         self.ingredients = ingredients
#         self.radius = radius
#         self.create_pizza()

#     def create_pizza(self):
#         print(f"Created ->  {self.name} with radius {self.radius} ingridients {self.ingredients}")
    
#     @classmethod
#     def create_pepperoni(cls, radius):
#         name = "Pepperoni"
#         ingredients = ("sausage", "chees", "dough", "origano")
#         return cls(name, radius, *ingredients)
    
#     @classmethod
#     def create_margarita(cls, radius):
#         name = "Margarita"
#         ingredients = ("pomodory", "chees", "dough", "origano")
#         return cls(name, radius, *ingredients)
    
#     @classmethod
#     def create_four_cheese(cls, radius):
#         name = "Four cheese"
#         ingredients = ("cheese another", "chees", "dough", "origano")
#         return cls(name, radius, *ingredients)

# Pizza.create_four_cheese(30)
# Pizza.create_margarita(30)
# Pizza.create_pepperoni(30)