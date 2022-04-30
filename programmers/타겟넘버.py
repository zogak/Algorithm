numbers= [4, 1, 2, 1]
target = 4
def solution(numbers, target):
    answer = 0
    sum = 0

    def dfs(idx, sum):
        print(idx)
        nonlocal answer
        if idx == len(numbers)-1:
            if sum == target:
                answer += 1
            return
        dfs(idx+1, sum+numbers[idx])
        dfs(idx+1, sum-numbers[idx])
    
    dfs(-1, sum)
    return answer

print(solution(numbers, target))