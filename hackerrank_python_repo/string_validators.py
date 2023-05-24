# Task: In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()

    is_alnum, is_alpha, is_digit, is_lower, is_upper = False

    for char in range(len(s)):
        if s[char].isalnum():
            is_alnum = True
        if s[char].isalpha():
            is_alpha = True
        if s[char].isdigit():
            is_digit = True
        if s[char].islower():
            is_lower = True
        if s[char].isupper():
            is_upper = True

    print(is_alnum)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)