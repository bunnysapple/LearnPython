RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

def test_subtract_one(result, input):
    COLOR = GREEN if result == input - 1 else RED
    print("\nExpected Value: {}{}".format(GREEN, input-1))
    print("{}Result: {}".format(COLOR, result))
    if result != (input - 1):
        print(f"{COLOR}Incorrect Value. Check your code and try again\n{NC}")
    else:
        print(f"{COLOR}Correct Value. Good Job.\n{NC}")

def test_subtract_these(result, num1, num2):
    COLOR = GREEN if result == num1 - num2 else RED
    print("\nExpected Value: {}{}".format(GREEN, num1-num2))
    print("{}Result: {}".format(COLOR, result))
    if result != (num1 - num2):
        print(f"{RED}Incorrect Value. Check your code and try again\n{NC}")
    else:
        print(f"{GREEN}Correct Value. Good Job.\n{NC}")