# We have seen that lists are mutable (they can be changed), 
# and tuples are immutable (they cannot be changed).

# Task: Read a given string, change the character at a given index and then print the modified string.

# mutate_string has the following parameters:
# - string string: the string to change
# - int position: the index to insert the character at
# - string character: the character to insert

# return string: the altered string
#######################################################
# Write a Python function that: (a) Takes a string as a parameter. 
# (b) Prints out each character followed by their index and the number of times character appears in the string (ignoring capitalization). 
# (c) For example, if you passed in 'HelloOo!!' to the function, the result would be: H (0) - 1 e (1) - 1 l (2) - 2 l (3) - 2 o (4) - 3 O (5) - 3 o (6) - 3 ! (7) - 2 ! (8) - 2

def string_info(s):
    count = 0
    for elem in s:
        if elem in s:
            count += 1
        else:
            count = 1
        print(elem, count)
    #return new_string

if __name__ == '__main__':
    s = input()
    s_new = string_info(s)
    print(s_new)