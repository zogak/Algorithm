import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tc = 0

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y: parent[y] = x
    else: parent[x] = y

while True:
    #TC
    n, m = map(int, input().split())
    tc += 1
    if n==0 and m==0: break
    
    visited = [0]*(n+1)
    parent = [i for i in range(n+1)]
    cycleParent = set()

    for _ in range(m):
        a, b = map(int, input().split())
        parentA = find_parent(parent, a)
        parentB = find_parent(parent, b)
        if parentA != parentB:
            union(parent, a, b)
        else:
            cycleParent.add(parentA)
    
    parentSet = set(parent[1:])
    cnt = len(parentSet)
    if cycleParent:
        cnt -= len(parentSet | cycleParent)

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')