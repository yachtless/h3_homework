import uuid
from logger import logger
from user import User


class Administrator(User):

    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()
        self.stop_words = ["bad", "revolting", "gross", "awful"]

    def __str__(self):
        return f"Admin {self.id}: {self.username} "

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)
        logger.debug("Supplies updated")

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)
        logger.debug("Orders updated")

    def check_order(self, order):
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                logger.info(f"Order [{order.id}] status: {order.status}")
                return order
        order.status = 'On hold'
        logger.info(f"Order [{order.id}] status: {order.status}")
        return order

    def check_review(self, review):
        for stop_word in self.stop_words:
            if stop_word in review.text.lower() or stop_word in review.header.lower():
                review.status = "Declined"
                logger.info(f"Review [{review.header}] status: {review.status}")
                break
        if review.status != 'Declined':
            review.status = "Published"
            logger.info(f"Review [{review.header}] status: {review.status}")
