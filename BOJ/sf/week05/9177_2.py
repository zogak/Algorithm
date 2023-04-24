'''
에휴 시간초과
'''
n = int(input())
def dfs(index, start):
    global indexList, res
    if index == len(word1):
        combinedList = list(combined)
        indexList.sort(reverse=True)
        for item in indexList:
            del combinedList[item]
        if ''.join(combinedList) == word2:
            res = 'yes'
        return

    for i in range(start, len(combined)):
        if word1[index] == combined[i]:
            indexList.append(i)
            dfs(index+1, i+1)
            indexList.remove(i)

for i in range(1, n+1):
    res = 'no'
    word1, word2, combined = input().split()

    indexList = []
    dfs(0,0)

    print(f'Data set {i}: {res}')