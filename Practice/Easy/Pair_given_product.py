# Pair with given product (Find if any pair exists)
# Given an array of distinct elements and a number x, find if there is a pair with a product equal to x.
input_str = input("Enter input array: ")
product = int(input("Enter product: "))
input_arr = [int(n) for n in input_str.split(",")]
all_pairs = []

for i in range(len(input_arr)):
    pairs = [(input_arr[i], j) for j in input_arr[i + 1: len(input_arr)] if (input_arr[i] * j) == product]
    if len(pairs) > 0:
        all_pairs.extend(pairs)
print(f"Yes\nPairs with the product equal to '{product}' are: {all_pairs}" if len(all_pairs) > 0 else "No")
