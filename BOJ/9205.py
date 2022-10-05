from collections import deque
import sys
input = sys.stdin.readline

def solution():
    LIMIT = 32768
    n = int(input())
    home_x, home_y = map(int, input().split())
    stores = []
    for i in range(n):
        store_x, store_y = map(int, input().split())
        stores.append((store_x, store_y))
    rock_x, rock_y = map(int, input().split())

    def getDistance(x1,y1,x2,y2):
        return abs(x1-x2) + abs(y1-y2)

    def bfs(start_x, start_y):
        q = deque()
        q.append((start_x, start_y))       
        visited = set()

        while q:
            x, y = q.popleft()
            if getDistance(x,y,rock_x,rock_y) <=1000:
                return "happy"
            else:
                for store in stores:
                    if store not in visited:
                        if getDistance(x,y,store[0],store[1]) <=1000:
                            visited.add(store)
                            q.append((store[0], store[1]))
        return "sad"

    return bfs(home_x, home_y)


t = int(input())
for _ in range(t):
    print(solution())

'''
1
2
0 0
1000 0
1000 1000
2000 1000
'''