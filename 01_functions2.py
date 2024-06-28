from test import test_subtract_one, test_subtract_these # This is me importing functions from elsewhere. Ignore this for now.

# We saw how a function is defined and I provided two examples of a function in the previous file.
# To recap, the first firnction was the return_number function which returned the number passed in and
# the second function was the add_one function which took in a number value and added one to it.

# Now it's time for you to try creating your own functions.

# Exercise 1:
# ------------------------------------------------------------------------------------------------ #
# Create a function named "subtract_one" which takes in one number value and returns one less than
# the value.


# Uncomment the next line before running the code.
# test_subtract_one(subtract_one(3), 3)
# ------------------------------------------------------------------------------------------------ #

# Exercise 2:
# ------------------------------------------------------------------------------------------------ #
# Create a function named "subtract_these" which takes in teo number values and returns the result of
# subtracting the first value with the second.
def subtract_these(num1, num2):
    return num1 - num2

# Uncomment the next line before running the code.
test_subtract_these(subtract_these(8, 4), 8, 4)
# ------------------------------------------------------------------------------------------------ #
