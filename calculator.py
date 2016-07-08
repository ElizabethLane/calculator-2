"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

exit_condition_not_reached = True

user_operation = raw_input(">>>")

while exit_condition_not_reached:
    try:

        parts_of_input = user_operation.split(" ")
        operation = parts_of_input[0]

        if operation == "+":
            sum_of_input = add(parts_of_input[1], parts_of_input[2])
            print sum_of_input

        elif operation == "-":
            difference_of_input = subtract(parts_of_input[1], parts_of_input[2])
            print difference_of_input

        elif operation == "*":
            product_of_input = multiply(parts_of_input[1], parts_of_input[2])
            print product_of_input
        
        else:
            print "Sorry, I don't understand this operation. Please try again."

        user_operation = raw_input(">>>")

    except IndexError: 
        print "That won't work, please put a space between all characters. \n e.g. + 5 5"
        exit_condition_not_reached = False
        user_operation = raw_input(">>>")
        exit_condition_not_reached = True