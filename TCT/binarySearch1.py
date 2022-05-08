def solution(n, m, tteok):
    tteok.sort()
    left, right = 0, tteok[-1]

    while left<=right :
        customer=0
        mid = (left+right)//2
        for t in tteok:
            if t > mid:
                customer += (t-mid)
            if customer >= m:
                break
        
        if customer > m :
            left = mid+1
        else:
            answer = mid
            right = mid - 1
    return answer

n = 4
m = 6
tteok = [19, 15, 10, 17]
print(solution(n, m, tteok))