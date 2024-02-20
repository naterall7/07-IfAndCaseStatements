###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def color_picker():
    answer = input("Please select a color from the rainbow, inferior human: ")
    match answer:
        case "red":
            print("Success! The inferior human has selected red! The color of inferior human blood!")
        case "orange":
            print("Success! The inferior human has selected orange! The color of fire!")
        case "yellow":
            print("Success! The inferior human has selected yellow! The color of the sun!")
        case "green":
            print("Success! The inferior human has selected green! The color of the grass!")
        case "blue":
            print("Success! The inferior human has selected blue! The color of the ocean!")
        case "indigo":
            print("Success! The inferior human has selected indigo! The color of the indigo plant!")
        case "violet":
            print("Success! The inferior human has selected violet! The color of the violet flower!")
        case other:
            print("Failure! Color is not on the rainbow!")
color_picker()

###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def grade():
    score = float(input("Please enter your percentage as a decimal: "))
    match score:
        case _ if 0.90 <= score < 1:
            print("You received a(n) A!")
        case _ if 0.80 <= score < 0.90:
            print("You received a(n) B!")
        case _ if 0.70 <= score < 0.80:
            print("You received a(n) C!")
        case _ if 0.60 <= score < 0.70:
            print("You received a(n) D!")
        case _ if score < 0.60:
            print("You received a(n) F!")
        case _:
            print("Invalid Score!")
grade()