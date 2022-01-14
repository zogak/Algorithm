import sys

sys.stdin = open("input.txt", "r")

def subtree(n):
    global cnt
    cnt += 1
    for i in range(2):
      if arr[i][n]:
          subtree(arr[i][n])

T = int(input())
for test_case in range(1, T + 1):
    e, n = map(int, input().split())
    arr = [[0 for _ in range(e+2)]for _ in range(2)]
    inputList = list(map(int, input().split()))

    for i in range(0, len(inputList), 2):
      parent, sibiling = inputList[i], inputList[i+1]
      if arr[0][parent]:
          arr[1][parent] = sibiling
      else:
          arr[0][parent] = sibiling
    
    cnt = 0
    subtree(n)
    print("#%d %d" % (test_case, cnt))