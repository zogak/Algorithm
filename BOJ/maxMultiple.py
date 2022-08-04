from decimal import Decimal
n = int(input())
graph = [Decimal(input()) for _ in range(n)]
dp = [0]*n

# for i in range(n):
#     l, r = i-1, i+1
#     value = graph[i]

#     while l>=0:
#         if graph[l] >= 1:
#             value *= graph[l]
#             l -= 1
#         else:
#             break

#     while r<n:
#         if graph[r] >= 1:
#             value *= graph[r]
#             r += 1
#         else:
#             break

#     dp[i] = value

# #print(round(max(dp), 3))
# #print('%0.3f' % max(dp))

for i in range(1, n):
    graph[i] = max(graph[i], graph[i-1]*graph[i])

print('%0.3f' % max(graph))