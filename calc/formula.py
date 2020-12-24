class Formula():

    def __init__(self):
        self._A = None
        self._oper = None
        self._B = None
        self._result = None

    def __str__(self):
        return f'{self.A} {self.oper} {self.B}'

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

    @property
    def oper(self):
        return self._oper

    @oper.setter
    def oper(self, value):
        if value in '+-/*':
            self._oper = value

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        self._B = value

    @property
    def awaiting_value(self):
        return self.A is not None and self.oper is not None and self.B is None

    def clear(self):
        self._A = None
        self._B = None
        self._oper = None
        self._result = None

    def perform_operation(self):
        if self.A is None:
            self.A = 0
        if self.B is None:
            self.B = 0
        if self.oper is None:
            return 0

        if self.oper == '+':
            return float(self.A) + float(self.B)
        elif self.oper == '-':
            return float(self.A) - float(self.B)
        elif self.oper == '/':
            return float(self.A) / float(self.B)
        elif self.oper == '*':
            return float(self.A) * float(self.B)