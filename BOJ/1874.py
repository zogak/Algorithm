'''
1874. 스택 수열
'''
def solution(array):
    stack = [1]
    ans = []
    for i in range(2, len(array)+1):
        if stack[-1] == array[-1]:
            stack.pop()
            ans.append('-')
            print('array:', array)
            print('stack:', stack)
        else:
            stack.append(i)
            ans.append('+')
            array.pop()
            print('array:', array)
            print('stack:', stack)

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

#[4, 3, 6, 8, 7, 5, 2, 1]
array.reverse()
#[1, 2, 5, 7, 8, 6, 3, 4]
ans = solution(array)
if ans:
    for char in ans:
        print(char)
else:
    print('NO')