# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample call to the function
sample_number = 5
result = factorial(sample_number)
print(f"Factorial of {sample_number} is: {result}")
