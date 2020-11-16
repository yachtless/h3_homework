import uuid
from user import User

class Administrator(User):

    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()
        self.stop_words = ["bad", "revolting", "gross", "awful"]

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

    def check_order(self, order):
        print(f"Checking order {order.id}")
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                return order
        order.status = 'On hold'
        return order

    def check_review(self, review):
        print(f"Checking review: [{review}]")
        for stop_word in self.stop_words:
            if stop_word in review.text.lower() or stop_word in review.header.lower():
                review.status = "Declined"
                break
        if review.status != 'Declined':
            review.status = "Published"
