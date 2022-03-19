def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]
        end = command[1]
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[command[2]-1])
    return answer