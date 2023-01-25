n = int(input())
ropes = list(int(input()) for _ in range(n))
ropes.sort(reverse=True)
temp = []
for i in range(n):
    temp.append(ropes[i]*(i+1))

print(max(temp))