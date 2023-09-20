def num_to_digits(num: int) -> list:
    return [int(ch) for ch in str(num)]


# def factorials(num: int):
#     fact = 1
#     if num <= 1:
#         return fact
#     for i in range(2, num + 1):
#         fact *= i
#     return fact


def is_strong_number(num: int):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return num == sum([facts[nd] for nd in num_to_digits(num)])


print([n for n in range(1000) if is_strong_number(n)])
