'''
1931. 회의실 배정
'''

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

schedule.sort(key = lambda x:x[0])
schedule.sort(key = lambda x:x[1])

endTime = 0
cnt = 0
for start, end in schedule:
	if start >= endTime:
		cnt += 1
		endTime = end

print(cnt)