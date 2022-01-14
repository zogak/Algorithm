'''
739. Daily Temperature
'''
T = [73, 74, 75, 71, 69, 72, 76, 73]
def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i-last
            print('answer->', answer)
        stack.append(i)
        print('stack->', stack)

    return answer

print(dailyTemperatures(T))
