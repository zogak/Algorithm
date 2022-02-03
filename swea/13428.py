'''
13428. 숫자 조작
런타임 에러
'''
n = '12345'
origin = list(map(int, n))
minAns = origin
maxAns = origin
ascend = sorted(origin)
descend = sorted(origin, reverse=True)

def solution(ans, flag):
	p, q = 0, 0
	while p < len(ans) and q < len(flag):
		if flag[q] == 0:
			q += 1
			continue
		if ans[p] == flag[q]:
			p += 1
			q += 1
			continue
		targetIdx = ans[p+1:len(ans)].index(flag[q]) + p + 1
		print('targetIdx:', targetIdx)
		print('p:', p)
		print(ans)
		ans[p], ans[targetIdx] = ans[targetIdx], ans[p]
		print(ans)
		break
	ans = list(map(str, ans))
	ret = "".join(ans)
	ret = int(ret)
	return ret

print(solution(minAns, ascend))
print(solution(maxAns, descend))