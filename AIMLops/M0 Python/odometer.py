def is_ascending_v1(n: int) -> bool:
    digits = num_to_digits(n)
    return all([a < b for a, b in zip(digits, digits[1:])])


def is_ascending_v2(n: int) -> bool:
    digits = num_to_digits(n)
    return list(sorted(set(digits))) == digits


def num_to_digits(num: int) -> list:
    return [int(ch) for ch in str(num)]


def next_reading_v1(reading: int):
    reading_len = len(num_to_digits(reading))
    reading += 1
    while not is_ascending_v2(reading):
        reading += 1
    return int(''.join(map(str, num_to_digits(reading)[:reading_len])))


print(next_reading_v1(789))