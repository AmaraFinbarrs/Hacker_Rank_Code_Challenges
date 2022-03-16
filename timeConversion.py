#Given a time in -hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):
    # Write your code here
        
    # length of the string
    n = len(s)

    # Extract the number part from the string
    s_number = s[:n - 2]
    # Extract the letter
    s_letter = s[-2:]

    # Split the number string at the colons to eliminate them
    s_split = s_number.split(':')
    #print(s_split)

    # to convert the string to integers to allow for easy calculation.
    # create an empty string
    s_calc = []
    for numbers in s_split:
        s_calc.append(int(numbers))  # a new string with the numbers
    #print(s_calc)

    if 'PM' in s:
        if abs(s_calc[0]) < 12:
            s_calc[0] += 12
    else:
        if abs(s_calc[0]) == 12:
            s_calc[0] -= 12
    #print(s_calc)

    # convert the integers back to string
    s_string = []
    for numbers in s_calc:
        numbers = str(numbers)
        if len(numbers) == 1:
            numbers = '0' + numbers
        s_string.append(numbers)
    #print(s_string)

    return ':'.join(s_string)
