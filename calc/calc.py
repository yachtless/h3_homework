import tkinter as tk
from formula import Formula


class Calculator(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.controls_layout = list()
        self.result_flag = False
        self.text_layout = [
            [],
            ['AC', '+/-', '%', '/'],
            ['7', '8', '9', 'X'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', None, ',', '=']
        ]
        self.callbacks_layout = [
            [],
            [self._bttn_AC, self._bttn_unary_minus, self._bttn_percent, self._bttn_divide],
            [self._bttn_7, self._bttn_8, self._bttn_9, self._bttn_multiply],
            [self._bttn_4, self._bttn_5, self._bttn_6, self._bttn_minus],
            [self._bttn_1, self._bttn_2, self._bttn_3, self._bttn_plus],
            [self._bttn_0, None, self._bttn_decimal, self._bttn_equals],
        ]
        self.display_stringvar = tk.StringVar()
        self.create_widgets()
        self.formula = Formula()

        print('init')

    def _bttn_AC(self):    # AC
        self.display_stringvar.set('0')
        self.formula.clear()

    def _bttn_unary_minus(self):    # +/-
        value = self.display_stringvar.get()
        if value.startswith('-'):
            value = value[1:]
        else:
            value = f"-{value}"
        self.display_stringvar.set(value)

    def _bttn_percent(self):    # %
        value = float(self.display_stringvar.get())
        self.display_stringvar.set(0.01 * value)

    def _bttn_plus(self):    # +
        self._press_op('+')

    def _bttn_minus(self):    # -
        self._press_op('-')

    def _bttn_multiply(self):    # *
        self._press_op('*')

    def _bttn_divide(self):    # /
        self._press_op('/')

    def _bttn_0(self):    # 0
        self._press_num(0)

    def _bttn_1(self):    # 1
        self._press_num(1)

    def _bttn_2(self):    # 2
        self._press_num(2)

    def _bttn_3(self):    # 3
        self._press_num(3)

    def _bttn_4(self):    # 4
        self._press_num(4)

    def _bttn_5(self):    # 5
        self._press_num(5)

    def _bttn_6(self):    # 6
        self._press_num(6)

    def _bttn_7(self):    # 7
        self._press_num(7)

    def _bttn_8(self):    # 8
        self._press_num(8)

    def _bttn_9(self):    # 9
        self._press_num(9)

    def _bttn_decimal(self):    # ,
        value = self.display_stringvar.get()
        if '.' not in value:
            value = f'{value}.'
        self.display_stringvar.set(value)

    def _bttn_equals(self):    # =
        self._press_op()

    def _press_num(self, num):
        value = self.display_stringvar.get()
        if value == '0' or self.result_flag:
            self.display_stringvar.set(num)
            self.result_flag = False
        else:
            self.display_stringvar.set(f"{value}{num}")

    def _press_op(self, oper=None):
        if self.formula.A and self.formula.B:
            self._perform_op(oper)
        elif self.formula.A:
            self.formula.B = float(self.display_stringvar.get())
            self._perform_op(oper)
        else:
            self.formula.A = float(self.display_stringvar.get())
            self.formula.oper = oper
            self.display_stringvar.set(0)
            print(self.formula)

    def _perform_op(self, oper=None):
        if oper:
            result = self.formula.perform_operation()
            print(result)
            self.formula.A = result
            self.formula.oper = oper
            self.formula.B = None
            self.display_stringvar.set(result)
            self.result_flag = True
            print(self.formula)
        else:
            result = self.formula.perform_operation()
            self.display_stringvar.set(result)
            self.result_flag = True
            self.formula.clear()
            print(self.formula)

    def create_widgets(self):
        layout_list = list()
        for row_num in range(6):
            inner_list = list()
            if row_num == 0:
                entry = tk.Entry(self, textvariable=self.display_stringvar, justify='right', width=40, state='disabled')
                inner_list.append(entry)
                entry.grid(row=0, column=0, columnspan=4)
            else:
                for col_num in range(4):
                    layout_value = self.text_layout[row_num][col_num]
                    if not layout_value:
                        continue
                    button = tk.Button(self, text=layout_value, height=3, width=10, activebackground='blue')
                    button['command'] = self.callbacks_layout[row_num][col_num]
                    inner_list.append(button)
                    if button['text'] == '0':
                        button.grid(row=row_num, column=col_num, columnspan=2)
                        button['width'] = 2 * button['width']
                    else:
                        button.grid(row=row_num, column=col_num)
            layout_list.append(inner_list)
        self.controls_layout = layout_list


root = tk.Tk()
calc = Calculator(root)
calc.grid_rowconfigure(2, weight=1)
calc.grid_columnconfigure(2, weight=1)
calc.mainloop()
