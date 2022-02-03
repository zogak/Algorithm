s = "a"
def solution(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    answer = []
    for i in range(1, len(s)//2+1):
        cnt = 1
        res = ''
        flag = s[0:i]
        #print('flag:', flag)
        for j in range(i, len(s), i):
            if s[j:j+i] == flag:
                #print('same')
                cnt += 1
            else:
                #print('different')
                if cnt == 1:
                    res += flag
                elif cnt > 1:
                    res += str(cnt) + flag
                flag = s[j:j+i]
                cnt = 1
        if cnt == 1:
            res += flag
        elif cnt > 1:
            res += str(cnt) + flag
        #print('res: ', res)
        answer.append(len(res))
    return min(answer)

ans = solution(s)
print(ans)