def is_leap(year):
    leap = False

    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        leap = True

        # year = 2100 needs to be false
        # year = 1992 needs to be true
        # year = 2400 needs to be true
        # year = 1990 needs to be false
    return leap

#year = 1992

print(is_leap(1990))