# Define a function named 'isPalindrome' that checks if a string is a palindrome
def isPalindrome(string):
    # Initialize left and right pointers to check characters from the start and end of the string
    left_pos = 0
    right_pos = len(string) - 1

    # Loop until the pointers meet or cross each other
    while right_pos >= left_pos:
        # Check if the characters at the left and right positions are not equal
        if not string[left_pos] == string[right_pos]:
            # If characters don't match, return False (not a palindrome)
            return False

        # Move the left pointer to the right and the right pointer to the left to continue checking
        left_pos += 1
        right_pos -= 1

    # If the loop finishes without returning False, the string is a palindrome, so return True
    return True


# Print the result of checking if the string 'aza' is a palindrome by calling the 'isPalindrome' function
print(isPalindrome('aza'))
