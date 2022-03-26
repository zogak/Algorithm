answers = [1, 2, 3, 4, 5]

def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    oneCnt, twoCnt, threeCnt = 0, 0, 0
    for i, a in enumerate(answers):
        if one[i%5] == a:
            oneCnt += 1
        if two[i%8] == a:
            twoCnt += 1
        if three[i%10] == a:
            threeCnt += 1
    
    howMany = [[oneCnt, 1], [twoCnt, 2], [threeCnt, 3]]
    howMany.sort(reverse = True)
    maxValue = howMany[0][0]
    for item in howMany:
        if item[0] == maxValue:
            answer.append(item[1])
    answer.sort()
    return answer

print(solution(answers))
