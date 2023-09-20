"""
Scenario
Some say that the Digit of Life is a digit evaluated using somebody's birthday.
It's simple - you just need to sum all the digits of the date.
If the result contains more than one digit, you have to repeat the addition until you get exactly one digit.
For example:
1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.
"""
dob_str = input("Enter DOB in any one oder ('YYYYMMDD' or 'DDMMYYYY' or 'MMDDYYYY'): ")
length = len(dob_str)
while length > 1:
    dob_str = str(sum([int(ch)for ch in dob_str]))
    length = len(dob_str)
print(dob_str)
