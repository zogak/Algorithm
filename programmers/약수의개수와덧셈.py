def solution(left, right):
    answer = 0

    # def count(num):
    #     cnt = 0
    #     for i in range(1, num + 1):
    #         if num%i == 0:
    #             cnt += 1
    #     return cnt
    
    def count(num):
        tmp = []
        cnt = 0
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                tmp.append(num%i)
                cnt += 1
                if i != (num//i):
                    tmp.append((num//i))
                    cnt += 1
        return cnt
            
    for num in range(left, right+1):
        if count(num)%2==0:
            answer += num
        else:
            answer -= num
    return answer

left, right = 13, 17
print(solution(left, right))