###############################################################################
# DONE: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def add(num1, num2):
    aresult = num1 + num2
    return aresult

def subtract(num1, num2):
    sresult = num1 - num2
    return sresult

def multiply(num1, num2):
    mresult = num1 * num2
    return mresult

def divide(num1, num2):
    dresult = num1 / num2
    return dresult

def if_calc():
    print("Hey, I'm a calculator! Don't believe me? Give me two numbers!")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Now please enter the symbol for the operation you would like to perform (+) Add (-) Subtract (*) Multiply (/) Division: ")
    if operation == "+":
        print("Addition, sounds good!")
        aresult = add(num1, num2)
        print(f"Addition: {aresult}")
        print("See, I told ya so!")
    elif operation == "-":
        print("Subtraction, sounds good!")
        sresult = subtract(num1, num2)
        print(f"Subtraction: {sresult}")
        print("See, I told ya so!")
    elif operation == "*":
        print("Multiplication, sounds good!")
        mresult = multiply(num1, num2)
        print(f"Multiplication: {mresult}")
        print("See, I told ya so!")
    elif operation == "/":
        print("Division, sounds good!")
        dresult = divide(num1, num2)
        print(f"Division: {dresult}")
        print("See, I told ya so!")
    else:
        print("Invalid Operation!")
if_calc()

###############################################################################
# DONE: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def case_calc():
    print("Hey, I'm a calculator! Don't believe me? Give me two numbers!")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Now please enter the symbol for the operation you would like to perform (+) Add (-) Subtract (*) Multiply (/) Division: ")
    match operation:
        case "+":
            print("Addition, sounds good!")
            aresult = add(num1, num2)
            print(f"Addition: {aresult}")
            print("See, I told ya so!")
        case "-":
            print("Subtraction, sounds good!")
            sresult = subtract(num1, num2)
            print(f"Subtraction: {sresult}")
            print("See, I told ya so!")
        case "*":
            print("Multiplication, sounds good!")
            mresult = multiply(num1, num2)
            print(f"Multiplication: {mresult}")
            print("See, I told ya so!")
        case "/":
            print("Division, sounds good!")
            dresult = divide(num1, num2)
            print(f"Division: {dresult}")
            print("See, I told ya so!")
        case other:
            print("Invalid Operation!")
case_calc()