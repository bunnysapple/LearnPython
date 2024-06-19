
def return_number(num):
    return num

# The above is an example of a function. Functions are reusable blocks of code that can be used
# in multiple places in your file, or even be imported out of your file to be used elsewhere.

# You can run/call the above function by calling it's name and passing in any value if necessary.
# Example:

print(return_number(9))

# If you run this code in the terminal, you will see that it prints out the number 9.

# Time to explain how to "define"(create) a function.

# First thing you see in the function above is the | def | keyword.
# This stands for "define" and is used to define a function. Simple as that.

# Next thing is the name of the function. This is up to you. You can name the function whatever you want.
# Realistically, you should be naming it based on what it does. Else it gets confusing real quick.

# After the name, you see the parenthesis, or brackets. In the brackets, you pass in any value you want
# to be available to use in the function.
# For example, in the function above, I need to use the value "num" inside the function, so I defined
# a value called "num" in the brackets to inform the interpreter that I require this value within the function.
# You can have functions with no values passed in. In such cases, you leave the brackets blank.

# You end the first line of defining a function with a colon(:).
# From the next line onwards, all the lines in the function are indented. This shows the interpreter that those
# lines of code are logic for the function instead of global(logic accessible everywhere in the file).
# If you do not indent, the function is not defined properly and it will cause bugs in your code.

# Something that a lot of functions do is return a value or result. This makes senseif you think about it.
# A function is reusable code that might take in a value and the result of the function might need to be returned/
# passed back out of the function.
# For example, When I called the function "return_number" inside the print function, I needed the return_number
# function to return the value to be then printed in the terminal.

# To return values from a function, you use the "return" keyword.

# Exercise:

def add_one(num):
    return num + 1

# ------------------------------------------------------------------------------------------------ #
# Above, I've defined a function "add_one". Using that as a template, can you define a function
# named "subtract_one" that takes in a number and returns a number one less than the number passed
# in?

# Tip: I've used an addition operator, "+", above. "-" operator is used for subtraction.
# Define function below:

# ------------------------------------------------------------------------------------------------ #

# Now that you've done that, run the code. If you do not remember how to run it, check
# "00_comments.py" file. Remember that this file is called "01_functions.py".