N, K = map(int, input().split())
names = list(input() for _ in range(N))
nameCntPerLength = [0]*21
res = 0

i = 0
for j in range(N):
    if j-i > K:
        nameCntPerLength[len(names[i])] -= 1
        i += 1
    
    res += nameCntPerLength[len(names[j])]
    nameCntPerLength[len(names[j])] += 1

print(res)