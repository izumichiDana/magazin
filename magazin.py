class Product:
    __id = 1

    def __init__(self, title, desc, price) -> None:
        self.id = Product.__id
        self.title = title
        self.desc = desc
        self.price = price
        Product.__id += 1

class Order:
    def error(self, user) -> None:
        print(f"sorry {user.name} u don't have enof money for pay u can add bill or delate some product")
        if input("add cash? (y):") == 'y':
            amount = int(input('vvedite summu: '))
            user.add_bill(amount)
    
    def __init__(self,user): 
            while user.bill < user.card.get('total_price'):
                self.error(user)
            user.bill -= user.card.get("total_price")
            print(f'vash zakaz edet po adressu{user.adress}')
            user.show_card()
            user.clear_card()
            print(f'u vas ostalos{user.bill} money')

class User:

    def __init__(self,name,adress) -> None:
        self.name = name 
        self.adress = adress
        self.bill = 0
        self.card = {"total_price":0}

    def add_bill(self,amount):
        self.bill += amount

    def add_to_card(self,*products):
        for product in products:
            self.card[product.id] = {"title":product.title,
                                    "price":product.price}
            self.card['total_price'] += product.price

    def remove_from_card(self,*products):
        for product in products:
            try:
                self.card.pop(product.id)
                self.card["total_price"] -= product.price
            except:
                print(f"{product.title} v vashei korzine net")

    def show_card(self):
        from pprint import pprint
        pprint(f'=================\n{self.name}')
        pprint(self.card)
        pprint("===================")   

    def clear_card(self):
        self.card.clear()
        self.card['total_price'] = 0         


ice_cream1 = Product("Magnat", "vkusnoe morojennoe",96)
ice_cream2 = Product('smak', 's kunjuyom',15)
plov = Product("plov","uzgen plov", 150)
salat = Product('shacarap', 'pomidor',50)

Nurkamila = User("Nurkamila","Alamedin 1")
Nurkamila.add_bill(1000)
Nurkamila.add_to_card(ice_cream1,salat,plov)


uluk = User('uluk','Tunguch')
uluk.add_bill(300)
uluk.add_to_card(ice_cream2,plov)


# Nurkamila.remove_from_cart(plov)
# # nurkamila.show_cart()

uluk_order = Order(uluk)