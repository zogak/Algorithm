N = int(input())
res = 0
nums = [1,2,3]

def isBad(word): #부분 순열 체크하는 법 인터넷 참고
    for i in range(1, len(word)//2+1):
        if word[-i:] == word[-2*i:-i]: return True
    return False

def dfs(cnt, word):
    global res
    if cnt == N:
        #res = min(res, int(word))
        print(word)
        exit(0) #여기에서 return으로 해주려면 어떻게 해야하는지?

    for i in range(3):
        if isBad(word+str(nums[i])) : continue
        dfs(cnt+1, word+str(nums[i]))

dfs(0,'')