import uuid


class Customer:
    def __init__(self, f_name, l_name, phone, email, dob):
        self.id = uuid.uuid4()
        self.first_name = f_name
        self.last_name = l_name
        self.phone = phone
        self.email = email
        self.date_of_birth = dob
        self.bonus_amount = 0

    def __str__(self):
        return f"Customer {self.id}: {self.first_name} {self.last_name}"

