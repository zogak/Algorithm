import sys
input = sys.stdin.readline
n, k, d = map(int, input().split())
boxes = []
for _ in range(k):
    start, end, gap = map(int, input().split())
    boxes.append(start)
    while True:
        start += gap
        if start <= end:
            boxes.append(start)
        else:
            break

boxes.sort()
res = 0
left, right = 0, len(boxes)-1

while left <= right:
    mid = (left+right)//2
    if mid+1 == d:
        res = boxes[mid]
        break
    elif mid+1 < d:
        mid = right + 1
    elif mid+1 > d:
        mid = left - 1

print(res)