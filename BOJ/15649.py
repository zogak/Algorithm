'''
n과m(1)
'''

# solution1
# from itertools import permutations

# n,m = map(int, input().split())
# number = [i for i in range(1, n+1)]
# permu = list(permutations(number, m))

# for per in permu:
#     print(' '.join(map(str, per)))


# solution2
n,m = map(int, input().split())
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str,tmp)))
        return
    
    for i in range(1, n+1):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()

dfs()