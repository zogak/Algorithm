'''
빌딩들을 하나씩 돌면서, 해당 빌딩의 왼쪽과 오른쪽을 각각 스택을 사용해서 구하는 식으로 접근했음.

n = int(input())
buildings = list(map(int, input().split()))

for i, building in enumerate(buildings):
    leftStack, rightStack = [], []
    for p in range(i):
        while leftStack and leftStack[-1][1] <= buildings[p]:
            leftStack.pop()
        if buildings[p] > building:
            leftStack.append((p,buildings[p]))

    for q in range(len(buildings)-1, i, -1):
        while rightStack and rightStack[-1][1] <= buildings[q]:
            rightStack.pop()
        if buildings[q] > building:
            rightStack.append((q,buildings[q]))

    stack = leftStack + rightStack
    visible = len(stack)
    if visible:
        if leftStack:
            res = leftStack.pop()[0]+1
        else:
            res = rightStack.pop()[0]+1
        print(visible, res)
    else:
        print(visible)
'''

'''
처음에 답을 저장할 배열을 만들어 둔 후에, 빌딩을 특정해서 좌, 우를 각각 보는 것이 아니라
좌->우 로 가는 것 쭉 보고, 우->좌 로 가는 것 쭉 보고 
하는 식으로 풀어야 함..
'''

