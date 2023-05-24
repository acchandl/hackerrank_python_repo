# We have seen that lists are mutable (they can be changed), 
# and tuples are immutable (they cannot be changed).

# Task: Read a given string, change the character at a given index and then print the modified string.

# mutate_string has the following parameters:
# - string string: the string to change
# - int position: the index to insert the character at
# - string character: the character to insert

# return string: the altered string

def mutate_string(string, position, character):
    x = position+1
    new_string = string[0:position] + character + string[x:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)