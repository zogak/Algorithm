from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
combi = list(combinations([i for i in range(n)], n//2))

res = 1e9
for i in range(len(combi)//2):
    start = combi[i]
    link = tuple(set([i for i in range(n)]) - set(start))

    start_score, link_score = 0, 0
    start_combi , link_combi = list(combinations(start, 2)), list(combinations(link, 2))

    for start in start_combi:
        start_score += (graph[start[0]][start[1]] + graph[start[1]][start[0]])
    
    for link in link_combi:
        link_score += (graph[link[0]][link[1]] + graph[link[1]][link[0]])

    score = abs(start_score - link_score)
    res = min(res, score)

print(res)