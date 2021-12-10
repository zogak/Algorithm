# 거리가 같은 것이 있으면 어떻게 할까??
import heapq
points = [[1,3],[-2,2], [3,1]]
k = 1

heap = []
for point in points:
    dist = point[0]**2 + point[1]**2
    heapq.heappush(heap, (dist, point[0], point[1]))

res = list()
for _ in range(k):
    (dist, x, y) = heapq.heappop(heap)
    res.append((x, y))
print(res)