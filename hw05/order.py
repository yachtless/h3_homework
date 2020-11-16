import uuid


class Order:
    def __init__(self, customer, item, amount):
        self.id = uuid.uuid4()
        self.customer = customer
        self.item = item
        self.amount = amount
        self.status = "New"

    def __str__(self):
        return f""


if __name__ == "__main__":
    