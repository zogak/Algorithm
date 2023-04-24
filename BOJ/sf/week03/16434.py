#아직 푸는중....
from math import ceil
n, hATK = map(int, input().split())
roomInfo = [list(map(int, input().split())) for _ in range(n)]
left, right = 1, int(1e9)
answer = 0
while left <= right:
    hhATK = hATK
    maxHP = (left+right)//2
    curHP = maxHP
    print(left, maxHP, right)

    flag = True

    for room in roomInfo:
        if room[0] == 1: #몬스터
            monsterATK, monsterHP = room[1], room[2] #몬스터 공격력, 생명력
            while True:
                monsterHP -= hATK #용사 먼저 공격
                if monsterHP <= 0:
                    break
                curHP -= monsterATK #몬스터 공격
                if curHP <= 0: #용사 죽음
                    flag = False
                    break

        elif room[0] == 2: #포션
            portionATK, portionHP = room[1], room[2]
            hhATK += portionATK
            curHP += portionHP
            if curHP > maxHP:
                curHP = maxHP

        if not flag:
            break

    if flag: # 용사 안죽음
        answer = maxHP
        right = maxHP - 1
    else:
        left = maxHP + 1

print(answer)
