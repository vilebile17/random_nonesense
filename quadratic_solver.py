print("Welcome to the quadratic solver,")
print("============================================")
correct = "n"

def check_if_num(var):
    if type(var) != int and type(var) != float:
        print("ERROR make sure what you typed was a proper number")
        return True
    else:
        return False

# This while loop is what takes the equation info from the user
while correct != "y":
    print("Firstly, what number is infront of the x^2?")
    try:
        a = int(input("If there is no number , just write 1 : "))
    except:
        print(f"There was an invalid number error. Make sure you typed the proper number")
        break

    print()
    print("What number is infront of the x?")
    try:
        b = int(input("If there is no x-term, just write 0 : "))
        if b > 0:
            written_b = f"+ {b}"
        else:
            written_b = f"{b}"
    except:
        print(f"There was an invalid number error. Make sure you typed the number properly") 
        break

    print()
    try:
        c = int(input("Finally, what is the number standing alone at the end? : "))
        if c > 0:
            written_c = f"+ {c}"
        else:
            written_c = c
    except:
        print(f"There was an invalid number error. Make sure you typed the number properly")
        break

    correct = input(f"So to confirm, your equation is {a}x^2 {written_b}x {written_c}? (y/n) : ")

