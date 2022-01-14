'''
5176. 
'''

import sys
sys.stdin = open("input.txt", "r")

def preorder(idx):
    global value
    if idx <= n:
        preorder(idx*2)
        tree[idx] = value
        value += 1
        preorder(idx*2 + 1)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0 for _ in range(n+1)]

    value = 1
    preorder(1)
    print("#{} {} {}".format(test_case, tree[1], tree[n//2]))