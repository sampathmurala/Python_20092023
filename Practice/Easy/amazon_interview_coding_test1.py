# In the given range [L, R], print all numbers having unique digits.
# e.g. In range 10 to 20 should print all numbers except 11.
def num_to_digits(num):
    return [int(n) for n in list(str(num))]


def unique_numbers(left, right):
    result = []
    for num in range(left, right+1):
        digits = num_to_digits(num)
        if len(digits) == len(set(digits)):
            result.append(num)
    return result


print(unique_numbers(21,100))