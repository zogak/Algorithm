n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    answer = 0
    def dfs(start):
        check[start] = 1
        for i in range(n):
            if computers[start][i] == 1 and check[i] == 0:
                dfs(i)

    check = [0]*n
    for i in range(n):
        if check[i]==0:
            answer += 1
            dfs(i)
    return answer

print(solution(n, computers))