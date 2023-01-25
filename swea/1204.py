'''
최빈수 구하기
'''
# from collections import Counter
# t = int(input())
# for _ in range(t):
#     test = int(input())
#     graph = list(map(int, input().split()))

#     c = Counter(graph)
#     c.sort(key = lambda x : (-x[1], -x[0]))
    
#     print('#{} {}'.format(test, c[0][0]))

t = int(input())
for _ in range(t):
    test = int(input())
    graph = list(map(int, input().split()))
    check = [0]*101
    for item in graph:
        check[item] += 1
    
    howMany = 0
    ans = 0
    for i, c in enumerate(check):
        if c >= howMany:
            howMany = c
            ans = i
            
    print('#{} {}'.format(test, ans))