numbers= [1, 1, 1, 1, 1]
target = 3
def solution(numbers, target):
    answer = 0
    sum = 0

    def dfs(idx, sum):
        nonlocal answer
        if idx == len(numbers)-1:
            print(sum)
            if sum == target:
                answer += 1
            return
        dfs(idx+1, sum+numbers[idx])
        dfs(idx+1, sum-numbers[idx])
    
    dfs(-1, sum)
    return answer

print(solution(numbers, target))