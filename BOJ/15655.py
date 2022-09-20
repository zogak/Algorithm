n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
tmp = []

def backtrack(start):
    if len(tmp) == m:
        print(*tmp)
        return
    
    for i in range(start, n):
        if nums[i] not in tmp:
            tmp.append(nums[i])
            backtrack(start+1)
            tmp.pop()

backtrack(0)