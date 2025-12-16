import math

class FixedPointIteration:
    def __init__(self):
        self.expr = input(
            "Enter g(x) using Python syntax\n"
            "g(x) = "
        )
        
        self.x0 = float(input("Enter initial guess x0: "))
        self.tol = 1e-6
        self.max_iter = 100

    def g(self, x):
        return eval(self.expr, {"x": x, "math": math})

    def iterate(self):
        print(f"{'Iter':<5}{'x':<20}")
        print("-" * 25)

        for i in range(self.max_iter):
            try:
                x1 = self.g(self.x0)

                # Prevent overflow / extremely large values
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

            if abs(x1 - self.x0) < self.tol:
                print("\nConverged to:", x1)
                return x1
            
            self.x0 = x1

        print("\nDid not converge.")
        return None

# Main method
if __name__ == '__main__':
    fpi = FixedPointIteration()
    fpi.iterate()
