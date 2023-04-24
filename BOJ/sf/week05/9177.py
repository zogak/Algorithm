'''
cat tree catrtee
케이스 커버 안됨.
'''
n = int(input())
for i in range(1, n+1):
    res = 'no'
    word1, word2, combined = input().split()

    word1Pointer = 0
    combinedPointer = 0
    indexList = []

    while combinedPointer < len(combined) and word1Pointer < len(word1):
        if word1[word1Pointer] == combined[combinedPointer]:
            indexList.append(combinedPointer)
            word1Pointer += 1
            combinedPointer += 1
        
        else:
            combinedPointer += 1

    if len(indexList) == len(word1):
        indexList.reverse()
        combinedInList = list(combined)
        for index in indexList:
            del combinedInList[index]
        print(combinedInList)
        if ''.join(combinedInList) == word2:
            res = 'yes'
    
    print(f'Data set {i}: {res}')


