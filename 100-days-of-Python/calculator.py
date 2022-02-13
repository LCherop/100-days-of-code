
from os import system
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a,b):
    """Adds two numbers"""
    return a + b
def sub(a,b):
    """Derives difference between two numbers"""
    return a - b
def mul(a,b):
    """Multiplies two numbers"""
    return a * b
def div(a,b):
    """Divides two numbers"""
    return a / b

ops = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
    print(logo)
    
    num1 = int(input("What's the first number?"))
    for symbol in ops:
            print(symbol)
    calculate = True


    while calculate:
        
        op = input("Pick an operation from the line above: ")

        num2 = int(input("What's the next number?"))

        calculation = ops[op]
        answer = calculation(num1,num2)

        print(f"{num1} {op} {num2} = {answer}")

        con = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit")
        
        if con == "y":
            num1 = answer
        else:
            calculate = False
            system('cls')
            calculator()
            
calculator()
