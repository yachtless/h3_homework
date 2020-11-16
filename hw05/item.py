import uuid


class Item:
    def __init__(self, title, description, price, colors=("Black", )):
        self.id = uuid.uuid4()
        self.title = title
        self.description = description
        self.price = float(price)
        self.colors = colors

    def __str__(self):
        return f"Item {self.id}: {self.title}, {self.price}"


if __name__ = '__main__':
    i1 = Item()