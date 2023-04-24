from collections import deque
N, K = map(int, input().split()) #map길이, k개 바이러스
#board 입력받기
board = []
q = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0: #바이러스
            q.append([tmp[j],i,j])
    board.append(tmp)
S, X, Y = map(int, input().split())
q.sort()
q = deque(q)
#좌표를 0,0부터 시작하기 위해 수정
X -= 1
Y -= 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(time):
    global board, q
    while q:
        length = len(q)
        time += 1
        for _ in range(length):
            virusNum, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or ny<0 or nx>=N or ny>=N: continue
                if board[nx][ny] != 0 : continue

                board[nx][ny] = virusNum
                q.append([virusNum,nx,ny])
        if time == S: return

time = 0
bfs(time)

if board[X][Y] == 0:
    print(0)
else:
    print(board[X][Y])