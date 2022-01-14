'''
5176. 
'''

import sys
sys.stdin = open("input.txt", "r")

def inorder(idx):
    global value
    if idx <= n:
        inorder(idx*2)
        tree[idx] = value
        value += 1
        inorder(idx*2 + 1)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0 for _ in range(n+1)]

    value = 1
    inorder(1)
    print("#{} {} {}".format(test_case, tree[1], tree[n//2]))

'''
3
6
8
15
'''