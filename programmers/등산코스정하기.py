from collections import deque

def solution(n, paths, gates, summits):
    INF = int(1e9)
    graph = {i:[] for i in range(1, n+1)}

    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))

    def getIntensity(start, end):
        intensities = [[]]
        visited = [0]*(n+1)
        q = deque()
        q.append(start)
        visited[start] = 1

        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                for item in graph[node]:
                    
                    # 이미 방문했거나 또다른 출입구라면 패스
                    if visited[item] == 1 or item in gates:
                        continue

                    q.append(item[0])
                    visited[item[0]] = 1
                    tmp = [item[1]]

                    for intensity in intensities:
                        intensity.append(tmp)

    answer = []
    min_intensity = INF
    for gate in gates:
        for summit in summits:
            intensity = getIntensity(gate, summit)
            
            #새로 구한 intensity 가 더 같거나 작으면 갱신
            if min_intensity >= intensity:
                min_intensity = intensity
                answer.append([min_intensity, summit])

    answer.sort(key = lambda x : (x[0], x[1]))
    ans_summit, ans_intensity = answer[0][1], answer[0][0]
    return [ans_summit, ans_intensity]