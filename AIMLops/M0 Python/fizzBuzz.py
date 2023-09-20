def fizzbuzz_v1(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    return n

#
# def fizzbuzz_game1(num: int) -> list:
#     return [fizzbuzz_v1(n) for n in range(1, num + 1)]


print([fizzbuzz_v1(n) for n in range(1, 21)])


def fizzbuzz_v2(n: int):
    output = ""
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    if output == "":
        output = n
    return output


print([fizzbuzz_v2(n) for n in range(1, 11)])


def fizzbuzz_v3(n: int):
    fbs = {
        (True, True) : "FizzBuzz",
        (True, False): "Buzz",
        (False, True): "Fizz",
        (False, False): n
    }
    return fbs[(n % 5 == 0, n % 3 == 0)]


print([fizzbuzz_v3(n) for n in range(1, 11)])


def pick_index(n: int):
    return 2*int(n % 3 == 0) + int(n % 5 == 0)


def fizzbuzz_v4(n: int):
    values = [n, "Buzz", "Fizz", "FizzBuzz"]
    return values[pick_index(n)]


print([fizzbuzz_v4(i) for i in range(1, 11)])