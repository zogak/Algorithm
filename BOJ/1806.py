N, S = map(int, input().split())
nums = list(map(int, input().split()))

j = 0
res = int(1e9)
sum_ = 0

for i in range(len(nums)):
    while sum_ < S and j < len(nums):
        sum_ += nums[j]
        j += 1

    if sum_ >= S:
        res = min(res, j-i)
    
    sum_ -= nums[i]

print(res if res != int(1e9) else 0)