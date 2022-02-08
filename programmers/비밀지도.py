n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
def solution(n, arr1, arr2):
    answer = []
    first_map = [[] for _ in range(n)]
    second_map = [[] for _ in range(n)]
    
    for i, num in enumerate(arr1):
        while num > 0:
            first_map[i].append(num%2)
            num = num // 2
        first_map[i].reverse()
        
        if len(first_map[i]) != n:
            tmp = n-len(first_map[i])
            for _ in range(tmp):
                first_map[i].insert(0, 0)
    for i, num in enumerate(arr2):
        while num > 0:
            second_map[i].append(num%2)
            num = num // 2
        second_map[i].reverse()

        if len(second_map[i]) != n:
            tmp = n-len(second_map[i])
            for _ in range(tmp):
                second_map[i].insert(0, 0)

    print(first_map)
    print(second_map)

    for i in range(n):
        res = ""
        for j in range(n):
            if first_map[i][j] == 1 or second_map[i][j] == 1:
                res += "#"
            elif first_map[i][j] == 0 and second_map[i][j] == 0:
                res += " "
        answer.append(res)
    return answer
print(solution(n, arr1, arr2))