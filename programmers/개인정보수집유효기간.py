def solution(today, terms, privacies):

    def getNextDayOfDueDate(since, howLong):
        yy,mm,dd = map(int,since.split("."))
        yy += howLong//12
        
        mm += (howLong - 12*(howLong//12))
        if mm <=12:
            pass
        else:
            mm -= 12
            yy += 1
        
        return yy,mm,dd
    
    answer = []
    info = {}
    todayYY, todayMM, todayDD = map(int, today.split("."))
    for term in terms:
        name, duration = term.split()
        info[name] = duration
    
    for i, privacy in enumerate(privacies):
        date, name = privacy.split()
        toyy, tomm, todd = getNextDayOfDueDate(date, int(info[name]))
        
        if toyy < todayYY:
            answer.append(i+1)
        elif toyy == todayYY:
            if tomm < todayMM:
                answer.append(i+1)
            elif tomm == todayMM:
                if todd <= todayDD:
                    answer.append(i+1)
        
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))