from collections import deque
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
q = deque(trucks)
 
bridge = deque([0] * w)
time = 0
 
while bridge:
    time += 1
    bridge.popleft()
    if q:
        if sum(bridge) + q[0] <= l:
            bridge.append(q.popleft())
        else:
            bridge.append(0)
print(time)