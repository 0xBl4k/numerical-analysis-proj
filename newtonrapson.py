# this file for newton-rapson method
import sympy as sp
class Newton:
    def __init__(self):
        self.fx = input("Enter your function ~$ f(x) => ")
        self.derivative()
        self.xN = float(input("\nEnter the value of first X (X node) => "))
        while True:
            match(int(input("""\nplease select they way
        1 - iteration
        2 - Error
        > """))): # just a case to choose from
                    case 1:
                        self.iter = int(input("\nHow many interations? => "))
                        self.tableIter()
                        break
                    case 2:
                        self.Error = float(input("\nWhat is the targeted Error? => "))
                        self.tableErr()
                        break
                    case _:
                        print("wrong number try again!")
    
    def derivative(self): # this is from where we get out derivative
        self.expr = sp.sympify(self.fx)
        self.derivative = sp.diff(self.expr, 'x')
        print(f"The derivative f'(x) is: {self.derivative}")

# this is Iteration
    def tableIter(self):
        print("\n| n |     Xn     |   f(Xn)    |   f'(Xn)   |    Xn+1    |")
        print("-----------------------------------------------------------")
        for n in range(0, self.iter):
            fxr = self.expr.subs('x', self.xN) # f(x)
            fxdr = self.derivative.subs('x', self.xN) # f'(x)
            xNN = self.xN - (fxr / fxdr) # Xn + 1 (aka new Xn) 
            print(f"| {int(n)} |  {self.xN: .5f}  |  {fxr: .5f}  |  {fxdr: .5f}  |  {xNN: .5f}   |")
            self.xN = xNN
        print(f"\nthe approximated root for this function is : {self.xN: .6f}")

# this is error
    def tableErr(self):
        print("\n| n |    Xn    |   f(Xn)   |  f'(Xn)    |     Xn+1     |   Error   |")
        print("----------------------------------------------------------------")
        n = 0
        while True:
            fxr = self.expr.subs('x', self.xN) # f(x)
            fxdr = self.derivative.subs('x', self.xN) # f'(x)
            xNN = self.xN - (fxr / fxdr) # Xn + 1 (aka new Xn) 
            Err = abs(xNN - self.xN) # calculating error 
            print(f"| {int(n)} |  {self.xN: .5f} | {fxr: .5f}  |  {fxdr: .5f}  |  {xNN: .5f}   | {Err: .5f}  |")
            self.xN = xNN
            n += 1 # just a counter its useless tbh but i putted it to represent the steps
            if Err <= self.Error: # checks if current error is equals or less then inputed error
                break
        print(f"\nthe approximated root for this function is : {self.xN: .6f}")
        
        
        
if __name__ == '__main__':
    Newton()