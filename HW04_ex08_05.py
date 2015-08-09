#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body
def count(string, letter):
	count = 0
	index = 0
	while index < len(string):
		if letter == string[index]:
			count = count + 1
			index = index + 1
		else:
			count = count
			index = index + 1
	print ("The letter '" + str(letter) + "' appears in the word '" + str(string) + "' " + str(count) + ' time(s).')



################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    #print("Hello World!") 
    count('emily','l')
    count('emily', 'z')
    count('mississippi','s')
    count('squirrelled','q')
    

if __name__ == '__main__':
    main()