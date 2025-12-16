# thats the main app file all other laws and methods will be created outside this file as a class using OOP
import fixedpoint
import newtonrapson
import secant
import bisection


if __name__ == '__main__':
    print("""hello user to begin with numerical solutions please choose a method by a number:
    1 - bisection
    2 - fixed point
    3 - newton rapson
    4 - secant""")
    while True:
        try:
            match(int(input("> "))):
                case 1: 
                    print("you have choosen bisection method!")
                    bisection.Bisection()
                    break
                case 2:
                    print("you have choosen fixed point method!")
                    fixedpoint.FixedPointIteration()
                    break
                case 3:
                    print("you have choosen newton rapson method!")
                    newtonrapson.Newton()
                    break
                case 4:
                    print("you have choosen secant method!")
                    secant.secant()
                    break
                case _:
                    print("you just entered wrong number please try again!")
        except ValueError: # if u entered string it gonna give u an error
            print("HEY! ONLY NUMBERS I SAID")

