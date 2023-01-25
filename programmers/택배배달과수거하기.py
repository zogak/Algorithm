def solution(cap, n, deliveries, pickups):
    i = n-1
    j = n-1
    
    while i >= 0 and deliveries[i]==0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1

    answer = 0 
    while i >= 0 or j >= 0:
        answer += (max(i,j)+1) * 2

        box = cap
        while i >= 0 and box:
            if deliveries[i] > box:
                deliveries[i] -= box
                box = 0
            else:
                box -= deliveries[i]
                deliveries[i] = 0
                while i >= 0 and deliveries[i] == 0:
                    i -= 1

        box = cap
        while j >= 0 and box:
            if pickups[j] > box:
                pickups[j] -= box
                box = 0
            else:
                box -= pickups[j]
                pickups[j] = 0
                while j >= 0 and pickups[j] == 0:
                    j -= 1
    return answer