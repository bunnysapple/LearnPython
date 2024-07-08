RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

def test_if_nums_same(func, num, arg):
    result = func(num)
    expected = num + 1 if arg == "add" else num - 1
    COLOR = GREEN if result == expected else RED
    print("\nExpected Value: {}{}".format(GREEN, expected))
    print("{}Result: {}".format(COLOR, result))
    if result != expected:
        print(f"{COLOR}Incorrect Value. Check your code and try again\n{NC}")
    else:
        print(f"{COLOR}Correct Value. Good Job.\n{NC}")

# def test_add(func, num1, num2=1):
#     result = func(num1, num2)
#     expected = num1 + num2 if
#     COLOR = GREEN if result == expected else RED
#     print("\nExpected Value: {}{}".format(GREEN, expected))
#     print("{}Result: {}".format(COLOR, result))
#     if result != expected:
#         print(f"{COLOR}Incorrect Value. Check your code and try again\n{NC}")
#     else:
#         print(f"{COLOR}Correct Value. Good Job.\n{NC}")

def test_opperation(func, num1, num2, arg):
        result = func(num1, num2)
        expected = (
            num1 + num2 if arg == "add" else num1 - num2 if arg == "minus"
            else num1 * num2 if arg == "multiply" else num1 / num2 if arg == "divide"
            else num1 ** num2 if arg == "exponent" else num1 // num2 if arg == "floor"
            else num1 % num2 if arg == "modulus" else 0
                    )
        COLOR = GREEN if result == expected else RED
        print("\nExpected Value: {}{}".format(GREEN, expected))
        print("{}Result: {}".format(COLOR, result))
        if result != expected:
            print(f"{COLOR}Incorrect Value. Check your code and try again\n{NC}")
        else:
            print(f"{COLOR}Correct Value. Good Job.\n{NC}")

class Test_Operator:
    def __init__(self, operation, arg):
        self.operation = operation
        self.arg = arg

    def test_one(self):
        test_if_nums_same(self.operation, 3, self.arg)
        test_if_nums_same(self.operation, 8, self.arg)
        test_if_nums_same(self.operation, 19, self.arg)

    def tests(self):
        test_opperation(self.operation, 2, 4, self.arg)
        test_opperation(self.operation, 11, 6, self.arg)
        test_opperation(self.operation, 10, 12, self.arg)
        test_opperation(self.operation, 4, 3, self.arg)
        test_opperation(self.operation, 9, 2, self.arg)
    
    