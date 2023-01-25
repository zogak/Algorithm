#solution1

# from itertools import combinations
# n,m = map(int, input().split())
# combi = list(combinations([i for i in range(1,n+1)], m))

# for com in combi:
#     print(' '.join(map(str,com)))

#solution2
# n,m = map(int, input().split())
# tmp = []

# def dfs():
#     if len(tmp) == m:
#         print(' '.join(map(str, tmp))) 
#         return
    
#     for i in range(1, n+1):
#         if not tmp:
#             tmp.append(i)
#             dfs()
#             tmp.pop()
#         else:
#             if i not in tmp and i > max(tmp):
#                 tmp.append(i)
#                 dfs()
#                 tmp.pop()

# dfs()

#solution3
n,m = map(int, input().split())
tmp = []

def dfs(node):
    if len(tmp) == m:
        print(' '.join(map(str, tmp))) 
        return
    
    for i in range(node, n+1):
        if i not in tmp:
            tmp.append(i)
            dfs(i+1)
            tmp.pop()

dfs(1)