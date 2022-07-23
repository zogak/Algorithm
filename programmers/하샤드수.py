def solution(x):
    x = str(x)
    sum = 0
    for char in x:
        sum += int(char)
    
    # if int(x)%sum == 0:
    #     return True
    # return False
    return int(x)%sum == 0


print(solution(10))