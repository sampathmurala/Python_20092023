def largest_num(number: str):
    return int("".join(sorted(list(number), reverse=True)))


def smallest_num(number: str):
    return int("".join(sorted(list(number))))


def next_num(number: str):
    return largest_num(number) - smallest_num(number)


def get_seq(num):
    seq = []
    prev, curr = 0, num
    while prev != curr:
        seq.append(curr)
        prev, curr = curr, next_num(str(curr))
    return seq


print(get_seq(1709))
print(get_seq(1812))

