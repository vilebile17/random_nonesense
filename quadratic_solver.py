import math

print("Welcome to the quadratic solver,")
print("============================================")
correct = "n"

def check_if_num(var):
    if type(var) != int and type(var) != float and type(var) != None:
        print("ERROR make sure what you typed was a proper number")
        return True
    else:
        return False

def solve_non_quadratic(b,c):
    # This function is basically just here as a little bit of fun if someone chooses to not put a x^2 coefficient 
    # 0 = bx + c
    # -c = bx
    # x = -c / b
    return -c/b

# This while loop is what takes the equation info from the user
while correct != "y":
    # This first part checks the x^2 coefficient
    print("Firstly, what number is infront of the x^2?")
    a, written_a = 0, "0"
    try:
        # This bit changes "written_a" depending on what the inputed "a" is. 
        a = int(input("If there is no number , just write 1 : "))
        if a == 1:
            written_a = "x^2"
        else: 
            written_a = f"{a}x^2"
    except:
        print(f"There was an invalid number error. Make sure you typed the number either as an integer or a decimal")
        break
    
    # This part checks the x coefficient
    print("==========================================")
    print("What number is infront of the x?")
    try:
        # This part changes "written_b" based on what "b" is
        b = int(input("If there is no x-term, just write 0 : "))
        if b > 0:
            written_b = f"+ {b}x"
        elif b == 1:
            written_b = "+x"
        else:
            written_b = f"- {abs(b)}x"
    except:
        print(f"There was an invalid number error. Make sure you typed the number either as an integer or a decimal") 
        break
    
    # This final part checks the constant at the end
    print("===========================================")
    try:
        # This bit changes "written_c" based on what "c" is
        c = int(input("Finally, what is the number standing alone at the end? : "))
        if c > 0:
            written_c = f"+ {c}"
        elif c == 0:
            written_c = ""
        else:
            written_c = f"- {abs(c)}"
    except:
        print(f"There was an invalid number error. Make sure you typed the number either as an integer or a decimal")
        break
    
    # confirms the equation from the user, if they say "n" it loops back to the beginning
    correct = input(f"So to confirm, your equation is 0 = {written_a} {written_b} {written_c}? (y/n) : ")
    if correct == "n":
        print()

# This next bit is what actually calculates the quadratic equations
# x = (-b +- sqrt(b^2 - 4ac) ) / 2a
nice_equation = True
try:
    denominator = 2 * a
except:
    nice_equation = False
    print(f"Err... That's not a quadratic equation... \n Anyway, the solution to that is x = {solve_non_qudratic(b,c)}")
try:
    square_root = math.sqrt(b**2 - 4*a*c)
    try:
        # remember, quadratic equations have two solutions
        numerator_one = -b + square_root
        numerator_two = -b - square_root
    except:
        nice_equation = False
        
    solution_one = numerator_one / denominator
    solution_two = numerator_two / denominator

except Exception as e:
    # This part deals with invalid square-roots
    if type(b) == int or type(b) == float:
        print(f"There was a {e}. The solution contains imaginary numbers which are too complex for my little brain")
    else:
        print("I think you typed the 'b' variable as a non-number")
    nice_equation = False

print("=====================================")

# Finally, this is what prints out the solutions
if nice_equation:
    if solution_one != solution_two:
        print(f"x = {solution_one} and x = {solution_two}")
    else: print(f"x = {solution_one}")
