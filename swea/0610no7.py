T = 1

def dfs(idx):
    if idx > N:
        return
    
    dfs(2*idx)
    print(arr[idx], end='')
    dfs(2*idx+1)


for tc in range(1, T+1):
    N = int(input())
    arr = [0]*(N+1)
    for _ in range(N):
        info = input().split()
        idx, val = info[0], info[1]
        arr[int(idx)] = val

    dfs(1)