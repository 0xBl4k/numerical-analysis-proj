# this file for secant method
import sympy as sp

class secant:
    def __init__(self):
        fx = input("Enter your function ~$ f(x) => ")
        self.expr = sp.sympify(fx)
        self.xNA = float(input("\nEnter the value of first X (X0) => "))
        self.xNB = float(input("Enter the value of first X (X1) => "))
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
    
    def tableIter(self):
        print("\n| n |     Xn     |     Xn-1     |   f(Xn)    |   f'(Xn-1)   |    Xn+1    |")
        print("---------------------------------------------------------------------------")
        for n in range(0, self.iter):
            fxA = float(self.expr.subs('x', self.xNA))
            fxB = float(self.expr.subs('x', self.xNB))
            xNN = float(self.xNB - ((fxB * (self.xNB - self.xNA))/(fxB - fxA)))
            print(f"| {int(n)} |  {self.xNB: .5f}  |  {self.xNA: .5f}  |  {fxB: .5f}  |  {fxA: .5f}  |  {xNN: .5f}   |")
            self.xNA = self.xNB
            self.xNB = xNN
        print(f"\nthe approximated root for this function is : {self.xNB: .6f}")
            

    def tableErr(self):
        print("\n| n |     Xn     |     Xn-1     |   f(Xn)    |   f'(Xn-1)   |    Xn+1    |  Error  |")
        print("--------------------------------------------------------------------------------------")
        while True:
            n = 0
            fxA = float(self.expr.subs('x', self.xNA))
            fxB = float(self.expr.subs('x', self.xNB))
            xNN = float(self.xNB - ((fxB * (self.xNB - self.xNA))/(fxB - fxA)))
            Err = abs(xNN - self.xNB)
            print(f"| {int(n)} |  {self.xNB: .5f}   |  {self.xNA: .5f}   |  {fxB: .5f}   |  {fxA: .5f}   |  {xNN: .5f}   |  {Err: .5f}  |")
            self.xNA = self.xNB
            self.xNB = xNN
            n += 1
            if Err <= self.Error:
                break
        print(f"\nthe approximated root for this function is : {self.xNB: .6f}")

if __name__ == '__main__': # this exist just to run only this file i dont want to run whole project i only want THIS FILE OK??
    secant()