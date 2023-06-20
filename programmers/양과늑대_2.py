def solution(info, edges):
    answer = 0
    visited = [0]*len(info)

    def dfs(sheep, wolf):
        nonlocal visited, answer
        if sheep <= wolf: return
        answer = max(answer, sheep)
        
        for parent, child in edges:
            if visited[parent] == 1 and visited[child] == 0:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                elif info[child] ==1 :
                    dfs(sheep, wolf+1)
                visited[child] = 0
    
    visited[0] = 1
    dfs(1,0)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))