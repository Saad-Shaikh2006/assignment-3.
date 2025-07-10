import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculations using the math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Displaying the results
print(f"✅ Square root of {num} is: {square_root}")
print(f"📉 Natural logarithm of {num} is: {natural_log}")
print(f"🌊 Sine of {num} (in radians) is: {sine_value}")
