# Variable definition and assignment
# n1 = 15
# n2 = 30

# Remove comments from the bottom lines to take input from the user
n1 = input('Enter value of x:  ')
n2 = input('Enter value of y:  ')

# Declaring a temporary variable and swapping values
temp = n1
n1 = n2
n2 = temp

# Print the output
print('The value of n1 after swapping: {}'.format(n1))
print('The value of n2 after swapping: {}'.format(n2))
