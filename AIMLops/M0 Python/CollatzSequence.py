def next_collatz(n):
    return n // 2 if n % 2 == 0 else (n * 3) + 1


def collatz_seq(number):
    if number == 4:
        return [4, 2, 1]
    else:
        return [number] + collatz_seq(next_collatz(number))


num = 1
res = collatz_seq(num)
print(res)
