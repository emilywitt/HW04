# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function
# You might want to use the built-in functions ord, which converts a character 
# to a numeric code, and chr, which converts numeric codes to characters.

# how do you cycle back through the beginning

# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Imports

# Body
def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a') # I get why we have to do this. but why is the return value 97?
    else:
        return letter
    #print start
    #print ord(letter)
    c = ord(letter) - start
    #print c
    i = (c+n)%26 + start
    #print i
    return chr(i)

def rotate_word(word, n):
    rotated_word = ''
    for letter in word:
        rotated_word = rotated_word + rotate_letter(letter,n) 
    return rotated_word
    


########
def main():

    #print rotate_letter("b", 13)
    print rotate_word("balk",13)
    print rotate_word('cheer', 7)
    print rotate_word('melon', -10)
    print rotate_word('melon', -26)


if __name__ == '__main__':
    main()  