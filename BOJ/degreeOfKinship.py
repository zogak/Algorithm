from collections import deque
n = int(input()) # total people number
target1, target2 = map(int, input().split())
m = int(input())
relation = {}
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    if not relation.get(x):
        relation[x] = list()
    if not relation.get(y):
        relation[y] = list()
    relation[x].append(y)
    relation[y].append(x)

def bfs():
    while q:
        person = q.popleft()

        if relation.get(person) is None:
            return False

        for item in relation.get(person):
            if visited[item] == 0:
                visited[item] = visited[person] + 1
                q.append(item)
    return True

if relation.get(target1) is None or relation.get(target2) is None:
    print(-1)

else:
    q = deque()
    if relation.get(target1) is not None:
        visited[target1] = -1
        for t in relation.get(target1):
            q.append(t)
            visited[t] = 1
        if not bfs() or visited[target2] == 0:
            print(-1)
        else:
            print(visited[target2])

    elif relation.get(target2) is not None:
        for t in relation.get(target2):
            visited[target2] = -1
            q.append(t)
            visited[t] = 1
        if not bfs() or visited[target1] == 0:
            print(-1)
        else:
            print(visited[target1])