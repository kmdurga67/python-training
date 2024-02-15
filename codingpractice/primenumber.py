def test_prime(n):
    # Check if 'n' is equal to 1
    if (n == 1):
        # If 'n' is 1, return False (1 is not a prime number)
        return False
    # Check if 'n' is equal to 2
    elif (n == 2):
        # If 'n' is 2, return True (2 is a prime number)
        return True
    else:
        # Iterate through numbers from 2 to (n-1) using 'x' as the iterator
        for x in range(2, n):
            # Check if 'n' is divisible by 'x' without any remainder
            if (n % x == 0):
                # If 'n' is divisible by 'x', return False (not a prime number)
                return False
        # If 'n' is not divisible by any number from 2 to (n-1), return True (prime number)
        return True


# Print the result of checking if 9 is a prime number by calling the 'test_prime' function
print(test_prime(9))
