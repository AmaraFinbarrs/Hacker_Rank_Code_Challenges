def lonelyinteger(a):
    # Write your code here
     # to sort the array
    result = 0
    
    for nums in a:
        result ^= nums
    return result