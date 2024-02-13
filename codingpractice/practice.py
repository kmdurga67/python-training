# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)


def fact(n):
    if n == 0:
        return 1
    else:
        p = 1
        for i in range(1, n+1):
            p = p*i
            i = i+1
        return p


number = int(input("Enter the number\n"))
result = fact(number)
print(f"The factorial of {number} is {result}")
