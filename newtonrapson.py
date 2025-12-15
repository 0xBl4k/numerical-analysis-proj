# this file for newton-rapson method
import sympy as sp
class Newton:
    def __init__(self):
        self.fx = input("Enter your function ~$ f(x) = ")
        x = sp.symbols('x')
        expr = sp.sympify(self.fx)
        self.derivative = sp.diff(expr, x)
        print(f"The derivative f'(x) is: {self.derivative}")
        self.x0 = input("Enter the value of first X (X node) = ")
    while True:
            match(int(input("""\nplease select they way
        1 - iteration
        2 - Error
    > """))):
                case 1:
                    self.iter = input("How many interations? = ")
                    break
                case 2:
                    self.Error = input("What is the targeted error?")
                    break
                case _:
                    print("wrong number try again!")
    def table(self):
        pass
        