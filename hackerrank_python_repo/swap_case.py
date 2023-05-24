def swap_case(s):
    new_string = ''
    # check each char in string
    for x in s:
        # check if char is lower or upper case and append it to the new_string
        if x == x.lower():
            new_string += x.upper()
        else:
            new_string += x.lower()

    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)