number_list = []
a = 0
b = 1 

for i in range(int(1000)):
    c = a + b
    a = b
    b = c
    number_list.append(c)
