#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math

# Body
def eval_loop():
	while True:
		u = raw_input('Enter an expression to be evaluated> ')
		if u == 'done':
			break
		n = eval(u)
		print n
	print n

# get an error message if the user doesn't input a proper expression (ie. strings)
# that can't be evaluated as integers. Is there any way to handle that without
# using Try? I think at this point in the material (ch 7) Try hasn't been covered
# yet so I'm thinking there should be?

################################################################################
def main():
    #pass # Remove this line and uncomment below once eval_loop is defined.
    eval_loop()
    

if __name__ == '__main__':
    main()