# --- Day 2: Integers and Floats ---

# Integer
num = 3
print(num)
print(type(num))  # <class 'int'>

# Float
number = 3.14
print(type(number))  # <class 'float'>

# Modulo operator (remainder after division)
print(223432 % 2)  # 0 means even, 1 means odd

# Augmented assignment
num += 10  # num = num + 10
print(num)  # 13

# String concatenation vs. integer addition
num1 = '10'
num2 = '20'
print(num1 + num2)  # '1020' (string concatenation)
num1 = int(num1)    # convert to integer
num2 = int(num2)    # convert to integer
print(num1 + num2)  # 30 (actual addition)

# Extra methods you explored
print(round(3.14159, 2))  # 3.14 (round to 2 decimal places)
print(abs(-5))            # 5 (absolute value)