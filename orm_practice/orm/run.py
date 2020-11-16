from customer import Customer
from supplier import Supplier
from item import Item
from supply import Supply
from order import Order
from admin import Administrator

supply = list()
orders = list()
items = list()

admin1 = Administrator("iamgod", "iamthelaw", "memyself@heavens.com")
supplier1 = Supplier("isupply", "4real", "Crab Shack Company", "Van Crabs",
                    "000-112-35-8", "crab@shack.biz")
supplier2 = Supplier("isupplytoo", "4real", "Reliable Company", "Van Reliable",
                    "011-112-35-8", "no-reply@reliable.biz")
customer1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                    "guido@python.org", "09-09-1968")
item1 = Item("Banana", "Better than ever before", 799.0,
            ("Golden", "Fresh Green"))
item2 = Item("Best Banana", "Better than others", 899.0,
            ("Truly Golden", "Fresher Green"))

supply.append(supplier1.add_supply(item1, 10))
supply.append(supplier2.add_supply(item2, 3))

customer1.create_order(item2, 5)
print(customer1.orders[0].status)

admin1.update_supply([supplier1, supplier2])
admin1.update_orders([customer1])

admin1.check_order(customer1.orders[0])
print(customer1.orders[0].status)

customer1.create_review('Superb header', 'Some awesome stuff!', 5)
customer1.create_review('Nice header', 'Some good stuff', 4)
customer1.create_review('Bad header', 'Not that good stuff', 3)
customer1.create_review('Even worse header', 'Some awful stuff', 2)
customer1.create_review('Gross header', 'Revolting stuff', 1)

for review in customer1.reviews:
    admin1.check_review(review)
    print(review)

print(customer1.reviews)
