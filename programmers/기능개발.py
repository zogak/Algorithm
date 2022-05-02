progresses = [20, 99, 93, 39, 55, 10]
speeds = [5, 10, 1, 1, 30, 5]
def solution2(progresses, speeds):
    answer = []
    days = []
    for i, progress in enumerate(progresses):
        if (100-progress) % speeds[i] != 0:
            days.append((100-progress)//speeds[i] + 1)
        else:
            days.append((100-progress)//speeds[i])
    
    print(days)
    stack = []
    for day in days:
        #커지면
        if stack and day > max(stack):
            answer.append(len(stack))
            stack.clear()
        stack.append(day)
    answer.append(len(stack))
    return answer

print(solution2(progresses, speeds))

