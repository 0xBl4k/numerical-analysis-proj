# this file for fixed-point method
import math

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    print(f"{'Iter':<5}{'x':<20}")
    print("-" * 25)

    for i in range(max_iter):
        try:
            x1 = g(x0)

            # prevent overflow / extremely large values
            if abs(x1) > 1e10:
                print("\nValue too large → possible overflow. Iteration stopped.")
                return None

        except OverflowError:
            print("\nOverflow error occurred. Try a different g(x) or x0.")
            return None
        except Exception:
            print("\nInvalid function input.")
            return None

        print(f"{i:<5}{x1:<20.10f}")

        if abs(x1 - x0) < tol:
            print("\nConverged to:", x1)
            return x1
        
        x0 = x1

    print("\nDid not converge.")
    return None
# main method 
if __name__ == '__main__':
    expr = input(
        "Enter g(x) using Python syntax\n"
        "Examples:\n"
        "  math.cos(x)\n"
        "  (x + 2) / 3\n"
        "  x**2 - 1\n"
        "  math.exp(-x)\n"
        "g(x) = "
    )

    def g(x):
        return eval(expr, {"x": x, "math": math})

    x0 = float(input("Enter initial guess x0: "))

    fixed_point_iteration(g, x0)
