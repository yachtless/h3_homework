import uuid


class Supply:
    def __init__(self, item, supplier, amount):
        self.id = uuid.uuid4()
        self.item = item
        self.supplier = supplier
        self.amount = amount

    def __str__(self):
        return f"{self.id}: {self.item} by {self.supplier}"

    def __repr__(self):
        return f"{self.id}: {self.amount} {self.item.title} by {self.supplier.company_name}"
