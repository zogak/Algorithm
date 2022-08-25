n = int(input())

answer = -1

if n <= 11:
    answer = n-1

else:
    index = 12
    answer = 20

    while True:
        if index == n:
            break

        if index == 1000000:
            answer = -1
            break

        answer += 1
        isDecreasing = True
        curr = str(answer)
        length = len(curr)
        for k in range(length-1):
            if curr[k] <= curr[k+1]:
                isDecreasing = False
                break
        
        if isDecreasing:
            index += 1

print(answer)