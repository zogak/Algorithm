import heapq

def solution(n, paths, gates, summits):
    INF = int(1e9)
    graph = {i:[] for i in range(1, n+1)}

    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))

    def getIntensity(start, end):
        intensities = [INF]*(n+1)
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, start))
        intensities[start] = 0

        while q:
            intensity, node =  heapq.heappop(q)

            for item in graph[node]:
                
                # 다른 출입구 중 하나라면 패스
                if item[0] in gates:
                    continue

                q.append((item[1], item[0]))
                if intensities[item[0]] > item[1]:
                    intensities[item[0]] = item[1]

        return intensities[end]

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