# Task: In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    substring_len = len(sub_string)
    results = 0

    for char in range(len(string)):
        # the 'print' below outputs all possible substrings
        # from left to right counting down the length of substring
        # output: abc, bcd, cdc, dcd, cdc,dc,c
        #print(new_string[char:char+substring_len])
        if string[char:char+substring_len] == sub_string:
            # count the number of occurrences 
            results += 1
    
    return results

if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = "In the convential world, it won't ever happen"
    sub_string = "lD,"

    count = count_substring(string, sub_string)
    print(count)