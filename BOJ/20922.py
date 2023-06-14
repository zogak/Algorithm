n, k = map(int, input().split())
nums = list(map(int, input().split()))

j = 0
res = 0
check = [0]*100001

for i in range(n):
    while j < n and check[nums[j]] < k:
        check[nums[j]] += 1
        j += 1

    res = max(res, (j-i))

    check[nums[i]] -= 1

print(res)