n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

orders = list(map(int, input().split()))

dice = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0
}

nx, ny = 0,0
dir = [(0,1), (0,-1), (-1,0), (1,0)]

def rollDice(order):
    if order == 1: #동
        dice['1'], dice['3'], dice['6'], dice['4'] = dice['4'], dice['1'], dice['3'], dice['6']
    elif order == 2: #서
        dice['1'], dice['3'], dice['6'], dice['4'] = dice['3'], dice['6'], dice['4'], dice['1']
    elif order == 3: #북
        dice['1'], dice['2'], dice['6'], dice['5'] = dice['5'], dice['1'], dice['2'], dice['6']
    elif order == 4: #남
        dice['1'], dice['2'], dice['6'], dice['5'] = dice['2'], dice['6'], dice['5'], dice['1']

for order in orders:
    # 1. 다음 위치 확인
    # 2. 구간 체크
    # 3. 주사위 돌리기
    
    nx = x + dir[order-1][0]
    ny = y + dir[order-1][1]

    # out of bound
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

    #roll the dice
    rollDice(order)

    # update current pos
    x = nx
    y = ny

    if graph[x][y] == 0:
        graph[x][y] = dice['6']
    else:
        dice['6'] = graph[x][y]
        graph[x][y] = 0

    print(dice['1'])