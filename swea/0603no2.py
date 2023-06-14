# 몇 개 테스트 케이스 통과가 안되는데 이유를 모르겠음.
# TC = int(input())
# for tc in range(1, TC+1):
#     res = 'OFF'
#     N, M = map(int, input().split())
#     M = bin(M)[2:]
#     lastBits = M[-N:]
    
#     if len(set(lastBits)) == 1:
#         if list(set(lastBits))[0] == '1':
#             res = 'ON'
#     print('#%d %s' %(tc, res))

TC = int(input())
for tc in range(1, TC+1):
    res = 'OFF'
    N, M = map(int, input().split())
    lastBits = (1<<N)-1
    
    if (lastBits&M) == lastBits:
        res = 'ON'
    print('#%d %s' %(tc, res))