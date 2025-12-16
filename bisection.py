import math

class Bisection:

    def __init__(self, tol=1e-6, max_iter=100):
        print("Enter your function in terms of x (example: x**3 - x - 2)")
        self.func_text = input("f(x) = ")

        self.a = float(input("Enter the left interval a: "))
        self.b = float(input("Enter the right interval b: "))

        if self.user_function(self.a) * self.user_function(self.b) >= 0:
            print("Bisection method fails. f(a) and f(b) must have opposite signs.")
            

        print("Iter |     a    |   b     |   c    |   f(c)   |")
        print("-----------------------------------------------")

        for i in range(1, max_iter + 1):
            c = (self.a + self.b) / 2
            fc = self.user_function(c)

            print(f"{i:4d} | {self.a:.6f} | {self.b:.6f} | {c:.6f} | {fc:.6f}   |")

            if abs(fc) < tol or abs(self.b - self.a) / 2 < tol:  
                print("\nApproximate root =", c)
                break

            if self.user_function(self.a) * fc < 0:
                self.b = c
            else:
                self.a = c

        print("Max iterations reached.")

    def user_function(self, x):
        return eval(self.func_text)

# main method
if __name__ == '__main__':
    Bisection()
