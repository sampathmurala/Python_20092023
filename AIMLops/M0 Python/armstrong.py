# def is_armstrong_v1(num):
#     total = 0
#     num_of_digits = len(str(num))
#     org_number = num
#     while num > 0:
#         total += (num % 10) ** num_of_digits
#         num = num // 10
#     return total == org_number
#

# def is_armstrong_v2(num):
#     num_of_digits = len(str(num))
#     return num == sum([(int(digit) ** num_of_digits) for digit in str(num)])


def num_to_digits(num: int) -> list:
    return [int(ch) for ch in str(num)]


def power(ds: list, k: int) -> list:
    return [d ** k for d in ds]


def is_armstrong_v3(num: int) -> bool:
    digits = num_to_digits(num)
    return num == sum(power(digits, len(digits)))


def get_armstrong_numbers(start: int, limit: int):
    return [n for n in range(start, limit + 1) if is_armstrong_v3(n)]


# print(power(num_to_digits(153), 3))
# print([n for n in range(100, 1000) if is_armstrong_v1(n)])
# print([n for n in range(100, 10000) if is_armstrong_v2(n)])
print(get_armstrong_numbers(10, 5000))
