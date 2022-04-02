number = "1924"
k =2
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        print('num:', num)
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            # 마지막 값이 새 값보다 작으면 pop하고
            while answer[-1] < num:
                print('in')
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    print('here')
                    break        
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

print(solution(number, k))