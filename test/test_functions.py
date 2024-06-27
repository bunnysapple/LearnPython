def test_subtract_one(result, input):
    print("Result: {}".format(result))
    print("Expected Value: {}".format(input-1))
    if result != (input - 1):
        print("Incorrect Value. Check your code and try again")
    else:
        print("Correct Value. Good Job.")

def test_subtract_these(result, num1, num2):
    print("Result: {}".format(result))
    print("Expected Value: {}".format(num1 - num2))
    if result != (num1 - num2):
        print("Incorrect Value. Check your code and try again")
    else:
        print("Correct Value. Good Job.")