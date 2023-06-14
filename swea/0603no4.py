T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        command = input().split()
        if command[0] == 'I':
            cmd, idx, val = command
            arr.insert(int(idx), int(val))
        elif command[0] == 'D':
            cmd, idx = command
            del arr[int(idx)]
        elif command[0] == 'C':
            cmd, idx, val = command
            arr[int(idx)] = int(val)

    if len(arr) < L-1: res = -1
    else: res = arr[L]

    print('#%d %d' %(tc, res))
    