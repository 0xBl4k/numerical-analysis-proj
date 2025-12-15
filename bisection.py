import math

# Convert user-typed function to something Python can calculate
def user_function(x, func_text):
    return eval(func_text)

def bisection_method(func_text, a, b, tol=1e-6, max_iter=100):

    if user_function(a, func_text) * user_function(b, func_text) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter |     a       b        c       f(c)")
    print("-----------------------------------------------")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = user_function(c, func_text)

        print(f"{i:4d} | {a:.6f}  {b:.6f}  {c:.6f}  {fc:.6f}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c

        if user_function(a, func_text) * fc < 0:
            b = c
        else:
            a = c

    print("Max iterations reached.")
    return c

# main method
if __name__ == '__main__':
    print("Enter your function in terms of x (example: x**3 - x - 2)")
    func_text = input("f(x) = ")

    a = float(input("Enter the left interval a: "))
    b = float(input("Enter the right interval b: "))

    root = bisection_method(func_text, a, b)
    print("\nApproximate root =", root)
