def solution(s):
    answer = 0
    xCnt, yCnt = 0,0
    for word in s:
        if xCnt == yCnt:
            x = word
            answer += 1
            print(x)
            print(xCnt, yCnt)
            print(answer)
        
        if x == word:
            xCnt += 1
        else:
            yCnt += 1
    return answer

print(solution("banana"))