def solution(n, t, m, timetable):
    answer = ''
    timeInMinute = []
    for time in timetable:
        hour, minute = time.split(':')
        hour, minute = int(hour), int(minute)
        timeInMinute.append(hour*60 + minute)
    timeInMinute.sort()
    
    print(timeInMinute)
    lastLeavingTime = 540 + (n-1)*t
    for i in range(n):
        leavingTime = 540 + i*t
        if leavingTime != lastLeavingTime:
            cnt = 0
            for crew in timeInMinute:
                if crew <= leavingTime:
                    timeInMinute.pop(0)
                    cnt += 1
                if cnt == m:
                    break
        #마지막 버스 탈 사람만 남아있는 상황
        if len(timeInMinute) < m:
            answerInMinute = leavingTime
        else:
            #현재 사람이 출발 시간보다 다 늦은 경우
            if timeInMinute[0] > leavingTime:
                answerInMinute = leavingTime
            #출발 시간 안과 밖 섞인 경우    
            elif timeInMinute[m-1] > leavingTime:
                answerInMinute = leavingTime
            #모두 출발 시간 안에 들어온 경우
            else:
                answerInMinute = timeInMinute[m-1]-1
    
    answer += str((answerInMinute // 60)).zfill(2) + ":" + str((answerInMinute % 60)).zfill(2)
        
    return answer

n, t, m = 2, 1, 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
print(solution(n, t, m, timetable))