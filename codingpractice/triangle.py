# to display stars in equilateral triangular form
n = 5
for i in range(1, 6):
    print(' '*n, end='')  # repet space for n times
    print('* '*(i))  # repeat stars for i times
    n -= 1


val = int(input("Enter the number:  "))
i = 1
j = 1
for i in range(1, val):
    for j in range(1, i+1):
        print(" * ", end="")
        j += 1
    print(" ")
    i += 1
