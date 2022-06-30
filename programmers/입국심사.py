# 기준 : 모든 사람이 심사를 끝내는데 걸리는 시간!
def solution(n, times):
    answer = 0
    left, right = min(times), max(times)*n
    while left <= right:
        people = 0
        mid = (left+right)//2
        for time in times:
            people += (mid//time)
            if people >= n:
                break
        
        if people >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        
    return answer