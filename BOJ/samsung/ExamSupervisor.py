n = map(int, input())
student = list(map(int, input().split()))
main, sub = map(int, input().split())

answer = 0
for s in student:
    
    # 한 반의 학생 수 <= 총감독 가능 수
    if s < main :
        answer += 1
        continue

    else:
        answer += 1
        if (s-main) % sub == 0:
            answer += (s-main) // sub
        else:
            answer += ((s-main) // sub + 1)

print(answer)