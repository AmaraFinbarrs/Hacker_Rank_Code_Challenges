
def fizzBuzz(n):
    # Write your code here
    for numbers in range(1, n + 1):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print('FizzBuzz')
        elif numbers % 3 == 0 and not numbers % 5 == 0:
            print('Fizz')
        elif numbers % 5 == 0 and not numbers % 3 == 0:
            print('Buzz')
        else:
            print(numbers)