'''
1991. 트리 순회
'''

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(current_node):
    print(current_node, end='')
    if tree[current_node][0] != '.':
        preorder(tree[current_node][0])
    if tree[current_node][1] != '.':
        preorder(tree[current_node][1])

def inorder(current_node):
    if tree[current_node][0] != '.':
        inorder(tree[current_node][0])
    print(current_node, end='')
    if tree[current_node][1] != '.':
        inorder(tree[current_node][1])

def postorder(current_node):
    if tree[current_node][0] != '.':
        postorder(tree[current_node][0])
    if tree[current_node][1] != '.':
        postorder(tree[current_node][1])
    print(current_node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')