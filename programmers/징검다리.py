def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 0, distance
    while left<=right:
        removed_rock = 0
        flag_rock = 0
        mid = (left+right)//2
        for rock in rocks:
            if rock-flag_rock < mid:
                removed_rock += 1
            else:
                flag_rock = rock
            if removed_rock > n:
                break
        
        if removed_rock > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer