# Setting inital variables
number_list = [0,1]
a = 0
b = 1 
counter = 0

fibonacci_number_count = int(input("how many fibonacci numbers do you want to check? : ")) - 2 

# Calculates the fibonacci numbers and puts them all in a list
for i in range(fibonacci_number_count):
    c = a + b
    a = b
    b = c
    number_list.append(c)

# this loop is what counts the threes
for number in number_list:
    power = 0
    str_number = str(number)

    # finds out how many digits are in each number
    while number > 10**power:
        power += 1
    
    # finally checks to see if the digit is a three
    for digit in str_number:
        if digit == "3":
            counter += 1

print(f"There are {counter} threes in the first {fibonacci_number_count + 2} fibonacci numbers")
