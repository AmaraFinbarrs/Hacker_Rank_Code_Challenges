def plusMinus(arr):
    # Write your code here

    # Create three empty arrays for the +ve values, -ve values and for the zero values.
    positive_val, negative_val, zero_val = [], [], []

    # Perform a for loop on the original array to add values to the new array according to type
    for number in arr:
        if number > 0:
            positive_val.append(number)
        elif number < 0:
            negative_val.append(number)
        else:
            zero_val.append(number)

    # calculate the ratio of the different types of numbers with respect to the original array.
    ratio_positive = len(positive_val) / len(arr)
    ratio_negative = len(negative_val) / len(arr)
    ratio_zero = len(zero_val) / len(arr)

    # output the ratio
    print('%.6f' % ratio_positive)
    print('%.6f' % ratio_negative)
    print('%.6f' % ratio_zero)

# try the code on examples
# n = 6
# arr = [-4, 3, -9, 0, 4, 1]
# plusMinus(arr)
