n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans1, ans2, ans3 = 0, 0, 0

def count(paper):
    global ans1, ans2, ans3
    size = len(paper)
    if size == 1:
        if paper[0][0] == -1: ans1 += 1
        elif paper[0][0] == 0 : ans2 += 1
        elif paper[0][0] == 1 : ans3 += 1
        return True
    elif size > 1:
        cnt1, cnt2, cnt3 = 0, 0, 0
        for i in range(size):
            for j in range(size):
                if paper[i][j] == -1:
                    cnt1 += 1
                elif paper[i][j] == 0:
                    cnt2 += 1
                elif paper[i][j] == 1:
                    cnt3 += 1

        if cnt1 == size*size:
            ans1 += 1
            return True
        elif cnt2 == size*size:
            ans2 += 1
            return True
        elif cnt3 == size*size:
            ans3 += 1
            return True
        

        #더 쪼개야함
        newSize = size // 3
        count([row[:newSize] for row in paper[:newSize]])
        count([row[newSize:newSize*2] for row in paper[:newSize]])
        count([row[newSize*2:] for row in paper[:newSize]])

        count([row[:newSize] for row in paper[newSize:newSize*2]])
        count([row[newSize:newSize*2] for row in paper[newSize:newSize*2]])
        count([row[newSize*2:] for row in paper[newSize:newSize*2]])

        count([row[:newSize] for row in paper[newSize*2:]])
        count([row[newSize:newSize*2] for row in paper[newSize*2:]])
        count([row[newSize*2:] for row in paper[newSize*2:]])

count(board)
print(ans1)
print(ans2)
print(ans3)