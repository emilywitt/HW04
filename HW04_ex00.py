#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program


# after user enters wrong guess, have to send back into asking for another input
# need to count the attempts (maybe use a while loop for this?)
# what if I make n the number of tries, and use while n <= 5?
################################################################################
# Imports
import random

# Body

def number_game():
	n = 0
	r = random.randint(1,25)
	#r = 15
	while n <= 4:
		g = raw_input ("You have " + str(5-n) +" chances to guess what number between 1 and 25 I'm holding behind my back.>")
		try:
			g == int(g)
			if int(g) == r:
				print "Great job!"
				return
			if int(g) < r:
				print ("Too Low")
			if int(g) > r:
				print ("Too High")
		except:
			print ("You just wasted one of your 5 chances. That's not even a number!")
		n = n + 1
	print "Sorry! You have run out of chances."
		

# after user enters wrong guess, have to send back into asking for another input
# need to count the attempts (maybe use a for loop for this, since number of attempts is a known quatity (would use while for unknown quantity?)?)
# what if I make n the number of tries, and use while n <= 5? and then employ a counter count = 0, each time through it becomes count = count + 1
# use a search for exiting when we find what we're looking for



################################################################################
def main():


    #print("Hello World!") # Remove this and replace with your function calls
    number_game()

if __name__ == '__main__':
    main()