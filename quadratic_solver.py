import math

print("Welcome to the quadratic solver,")
print("============================================")
correct = "n"

def check_if_num(var):
    if type(var) != int and type(var) != float:
        print("ERROR make sure what you typed was a proper number")
        return True
    else:
        return False

def solve_non_quadratic(b,c):
    # 0 = bx + c
    # -c = bx
    # x = -c / b
    return -c/b

# This while loop is what takes the equation info from the user
while correct != "y":
    print("Firstly, what number is infront of the x^2?")
    try:
        a = int(input("If there is no number , just write 1 : "))
        if a == 1:
            written_a = ""
        else: 
            written_a = f"{a}"
    except:
        print(f"There was an invalid number error. Make sure you typed the number either as an integer or a decimal")
        break

    print("==========================================")
    print("What number is infront of the x?")
    try:
        b = int(input("If there is no x-term, just write 0 : "))
        if b > 0:
            written_b = f"+ {b}"
        elif b == 1:
            written_b = "+"
        else:
            written_b = f"{b}"
    except:
        print(f"There was an invalid number error. Make sure you typed the number either as an integer or a decimal") 
        break

    print("===========================================")
    try:
        c = int(input("Finally, what is the number standing alone at the end? : "))
        if c > 0:
            written_c = f"+ {c}"
        else:
            written_c = c
    except:
        print(f"There was an invalid number error. Make sure you typed the number either as an integer or a decimal")
        break

    correct = input(f"So to confirm, your equation is {written_a}x^2 {written_b}x {written_c}? (y/n) : ")

# x = (-b +- sqrt(b^2 - 4ac) ) / 2a
nice_equation = True
try:
    denominator = 2 * a
except:
    nice_equation = False
try:
    square_root = math.sqrt(b**2 - 4*a*c)
    try:
        numerator_one = -b + square_root
        numerator_two = -b - square_root
    except:
        print("Err... That's not a quadratic equation...")
        print("Anyway, the solution to that is x = {solve_non_quadratic(b,c)}")
        nice_equation = False

except Exception as e:
    if type(b) == int or type(b) == float:
        print(f"There was a {e}. The solution contains imaginary numbers which are too complex for my little brain")
    else:
        print("I think you typed the 'b' variable as a non-number")
    nice_equation = False

print("=====================================")

if nice_equation:
    if solution_one != solution_two:
        print(f"x = {solution_one} and x = {solution_two}")
    else: print(f"x = {solution_one}")
