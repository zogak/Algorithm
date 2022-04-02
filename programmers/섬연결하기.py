n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
def solution(n, costs):
    # kruskal algorithm
    # 탐욕적인 방법을 이용하여 가중치를 간선에 할당한 그래프의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것

    #1. 그래프의 간선을 가중치의 오름차순으로 정렬
    #2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택
    #3. 해당 간선을 현재의 MST 집합에 추가
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                print('routes', routes)
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                print('costs',costs)
                break
    return ans

print(solution(n, costs))