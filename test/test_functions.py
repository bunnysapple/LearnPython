def test_subtract_one(function, input):
    print("Result: {}".format(function))
    print("Expected Value: {}".format(input-1))
    if function != (input - 1):
        print("Incorrect Value. Check your code and try again")
    else:
        print("Correct Value. Good Job.")