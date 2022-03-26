import itertools

given = [6, 10, 2]

res = list(map(list, itertools.permutations(given, 3)))
print(res)


print(res)
temp = []
for item in res:
    item = list(map(str, item))
    temp.append(''.join(item))
print(temp)

print(max(temp))