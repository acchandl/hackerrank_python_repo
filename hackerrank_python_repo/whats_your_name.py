#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
# final output should be "Hello firstname lastname! 
# You just delved into python."

def print_full_name(first, last):
    result = "Hello {} {}! You just delved into python.".format(first,last)
    
    print(result)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)