a, b, counter, number_list =  0, 1, 0, [0,1]
fibonacci_number_count = int(input("how many fibonacci numbers do you want to check? : ")) - 2 
for i in range(fibonacci_number_count):
    c = a + b
    a, b = b, c
    number_list.append(c)
for number in number_list:
    power, str_number = 0, str(number)
    while number > 10**power:
        power += 1
    for digit in str_number:
        if digit == "3":
            counter += 1
print(f"There are {counter} threes in the first {fibonacci_number_count + 2} fibonacci numbers")
