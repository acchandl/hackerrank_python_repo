# Task: Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.
# The first line contains n (the total number of scores). 
# The second line contains an array A[] of n integers each separated by a space.

import array as arr

if __name__ == '__main__':
    n = int(input("Enter number of scores: "))
    arr = map(int, input().split()) 

    print(n)

    # to solely print the array items:
    # need to turn the arr map into a list or tuple or you'll get output like: <map object at 0x7fcbe49f0fa0>
    # so do: print(list(arr))

    # sort the array
    sorted_arr = list(arr).sort

    print(sorted_arr)

    scores = []
    for i in range(0,n):
        scores.append(arr) # add the elements here



    #print(number_of_scores)


        #print (a[i], end =" ")
  
