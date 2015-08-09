#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """if the first letter of the string is uppercase, this returns FALSE becuase the first
    time through the IF condition is not met, so it goes on to the ELSE statement which
    automatically returns FALSE. 
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
        print c

def any_lowercase2(s):
    """isn't this just checking if the string 'c' is lowercase? which it always will be because
    it is given as lower. If you change it to 'C'.islower() then it always returns FALSE. The
    only time this doesn't return TRUE is if there are no characters in the string..
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """this just returns TRUE or FALSE for whether or not the last character in the string is
    uppercase or lowercase.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """I don't understand this one.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """as it goes through the letters, as soon as it gets to an uppercase letter
    it returns FALSE. therefore it is looking for any upper, not any lower
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    print any_lowercase5("thisstring")
    print any_lowercase5("ThisstringmessesupthefunCtion")
    

if __name__ == '__main__':
    main()