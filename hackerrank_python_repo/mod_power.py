# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). 
# On the second line, print the result of pow(a,b,m)
# Note: pow(a,b,m) is a^b mod m
# Note: Here, a and b can be floats or negatives, but, if a third argument is present, m cannot be negative.
a = int(input())
b = int(input())
m = int(input())

def mod_power(a,b,m):
    print(a**b)
    if (m >= 0):
        print(pow(a,b,m))

mod_power(a,b,m)