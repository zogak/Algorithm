import math
def solution(fees, records):
    basicTime, basicCost, unitTime, unitCost = fees[0], fees[1], fees[2], fees[3]
    answer = []
    info = {}
    temp = []
    for record in records:
        time, carNum, behave = record.split()
        if behave=="IN":
            info[carNum] = time
        else:
            # info에서 같은 carNum 찾아서 시간 계산 한 후에 temp에 (carNum, cost)로 저장
            inTime, outTime = info[carNum], time
            inTimeH, inTimeM = inTime.split(':')
            outTimeH, outTimeM = outTime.split(':')
            inTimeInMin = inTimeH*60+inTimeM
            outTimeInMin = outTimeH*60+outTimeM

            diff = outTimeInMin - inTimeInMin
            if diff <= basicTime:
                cost = basicCost
            else:
                cost = basicCost
                cost += math.ceil((diff-basicTime)/unitTime)*unitCost
    
            temp.append((cost, carNum))
            info.pop(carNum)
    
    


    return answer