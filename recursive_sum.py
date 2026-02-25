## Asiwome Agbleze
## CMSC 111
## Srping 2026

# This recursive function return the sum of all integers from 1 to n
def recursive_sum(n):
    # Base case: if n is 1, the sum from 1 to 1 is just 1
    if n == 1:
        return 1
    

    # Recursive case: sum from 1 to n is n plus the sum from 1 to n-1
    return n + recursive_sum(n - 1)


# Ask the user for value of n
user_input = input("Enter a value for n: ")


# Convert the input string to an integer
n = int(user_input)

# Calculate the sum using the recursive function
result = recursive_sum(n)


# Print the result in a clear message
print("The sum from 1 to", n, "is:", result)