a = '9875'
y = [int(x) for x in list(a * 10)]
print(str(sum(y)))
k = 4
while True:
    if len(a) == 1:
        a = int(a)
        print(a)
        break
    else:
        a = [int(x) for x in list(a * k)]
        a = str(sum(a))
        # print(a)


def super_digits(n, k):
    # we find p
    
    p = n * k

    # we create a loop that converts p to a list and
    # then convert individual elements to integers
    # we stop this operation when p has only one element
    while True:  # create a loop
        if len(p) == 1:  # p has only one element
            print(p)
            print(int(p))  # convert p to integer and return the value
            break  # stop the loop here because we have found the super digit
        else:
            p = [int(x) for x in list(p)]  # convert p to  list of integers
            p = str(sum(p))  # convert the sum of integers in the loop to a string
            print(p)


# solution using recursion. From YouTube [Hackers Realm]
def super_digits2(n, k):
    def helper(n):
        total = 0
        for num in n:
            total += int(num)
        total = str(total)
        if len(total) == 1:
            return print(total)
        else:
            return helper(total)

    p = str(helper(n)*k)  # formerly p = str(n)*k
    return helper(p)

# for example, we have input 123 3
# 123123123
# helper(123123123)
# total = 1+2+3+1+2+3+1+2+3 = 18
# helper(18)
# total = 1 + 8 = 9
# return 0 (as it's only one digit)
# not an optimized solution

# helper(123)
# total = 1+2+3
# p = 666
# helper(666)
# total = 6+6+6 = 18
# helper(1+8) = 9
# total = 1+ 8
# return 9 (as it's only one digit)


super_digits2('9875', 0)
