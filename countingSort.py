def countingSort(arr):
    # Find the maximum number
    max_arr = max(arr)
    
    # create an empty array for storing the frequency of numbers
    freq_arr = [0]*100

    for nums in arr:
        freq_arr[nums] += 1
    return freq_arr