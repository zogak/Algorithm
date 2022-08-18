n, m = map(int, input().split())
trees = list(map(int, input().split()))

l, r = 0, max(trees)
ans = 0
while l<=r:
    mid = (l+r)//2
    obtained = 0

    for tree in trees:
        if tree > mid:
            obtained += (tree-mid)

    if obtained >= m:
        ans = max(ans, mid)
        l = mid+1
    
    else:        
        r = mid-1

print(ans)