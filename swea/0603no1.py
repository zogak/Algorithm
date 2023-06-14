# 방법1. set 사용
## 방법1. str로 바꾸어 각 자리수를 구하는 방법 사용
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    uniqueNums = set()
    cnt = 0
    while len(uniqueNums) < 10:
        cnt += 1
        num = cnt*N
        for num in str(num):
            uniqueNums.add(num)
    print('#%d %d' %(tc, cnt*N))

## 방법2. 10으로 나누어 맨 뒤 숫자부터 가져오는 일반적인 방법 사용
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    uniqueNums = set()
    cnt = 0
    while len(uniqueNums) < 10:
        cnt += 1
        num = cnt*N
        while num > 0:
            uniqueNums.add(num%10)
            num = num//10
    print('#%d %d' %(tc, cnt*N))

#2. 방법2. set말고 check배열을 사용. cnt 변수도 도입
#         cnt 변수 도입으로 인해 기존 답에 사용하던 cnt를 res가 대체
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [0]*10
    cnt = 0
    res = 0
    while cnt < 10:
        res += 1
        num = res*N
        for num in str(num):
            num = int(num)
            if not check[num]:
                check[num] = 1
                cnt += 1

    print('#%d %d' %(tc, res*N))

