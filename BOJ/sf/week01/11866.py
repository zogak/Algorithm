n, k = map(int, input().split())

people = [i for i in range(1, n+1)]
answer = []
index = 0
while people:
    index = (index+k-1)%len(people)
    answer.append(people[index])
    del people[index]


res = "<"
for a in answer:
    res += str(a)
    res += ', '
res = res[:-2]
res += ">"
print(res)