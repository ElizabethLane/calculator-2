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

        if len(parts_of_input) == 3:

            if operation == "+":
                sum_of_input = add(parts_of_input[1], parts_of_input[2])
                print sum_of_input

            elif operation == "-":
                difference_of_input = subtract(parts_of_input[1], parts_of_input[2])
                print difference_of_input

            elif operation == "*":
                product_of_input = multiply(parts_of_input[1], parts_of_input[2])
                print product_of_input

            elif operation == "/":
                quotient_of_input = divide(parts_of_input[1], parts_of_input[2])
                print quotient_of_input

            elif operation == "pow":
                power_of_input = power(parts_of_input[1],parts_of_input[2])
                print power_of_input

            elif operation == "mod":
                mod_of_input = mod(parts_of_input[1], parts_of_input[2])
                print mod_of_input

        elif len(parts_of_input) == 2:    
            
            if operation == "square":
                square_of_input = square(parts_of_input[1])
                print square_of_input

            elif operation == "cube":
                cube_of_input = cube(parts_of_input[1])
                print cube_of_input
        
        else:
            print "Sorry, I don't understand this operation. Please try again."

        user_operation = raw_input(">>>")

    except IndexError: 
         print "That won't work, please put a space between all characters. \n e.g. + 5 5"
         user_operation = raw_input(">>>")
