# Write a program that prints the minimum and maximum values that can
# be calculated by summing exact four of the five integers.
# it prints the respective values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    
    # Firstly I sort the array or list
    arr.sort()

    min_value_sum = sum(arr[:4])  # the first four print the min value because it is sorted
    max_value_sum = sum(arr[1:])  # the last four print the max value because it is sorted
    
    # prints the output as two space-separated long integers.
    print(min_value_sum, max_value_sum)