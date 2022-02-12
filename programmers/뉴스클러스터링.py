import collections
str1 = "aa1+aa2"
str2 = "AAAA12"
def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    setForStr1, setForStr2 = [], []
    for i in range(len(str1)-1):
        setForStr1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        setForStr2.append(str2[i:i+2])
    
    #print(setForStr1)
    #print(setForStr2)
    setForStr1Cleared, setForStr2Cleared = [], []
    for str in setForStr1:
        if str.isalpha():
            setForStr1Cleared.append(str)
    
    for str in setForStr2:
        if str.isalpha():
            setForStr2Cleared.append(str)

    #print(setForStr1Cleared)
    #print(setForStr2Cleared)

    setForStr1Cleared = collections.Counter(setForStr1Cleared)
    setForStr2Cleared  = collections.Counter(setForStr2Cleared)

    intersection = list((setForStr1Cleared & setForStr2Cleared).elements())
    union = list((setForStr1Cleared | setForStr2Cleared).elements())

    #print(intersection)
    #print(union)

    if len(union) == 0:
        answer = 65536
    else:
        answer = int((len(intersection) / len(union)) * 65536)

    return answer

solution(str1, str2)