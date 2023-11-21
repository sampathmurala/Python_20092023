arr = [1, 3, 0, 2, 5]
result = ['_']

for i in range(1, len(arr)):
    result.append([j if j < arr[i] else "_" for j in (arr[:i])][-1])
print(result)
