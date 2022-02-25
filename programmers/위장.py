clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["pink_blouse", "shirt"]]

def solution(clothes):
    answer = 1
    clothesInfo = dict()
    for item in clothes:
        if item[1] not in clothesInfo:
            clothesInfo[item[1]] = list()
        clothesInfo[item[1]].append(item[0])

    print(clothesInfo)

    for item in clothesInfo.values():
        answer *= (len(item) + 1)
    
    answer = answer - 1
   
    return answer

print(solution(clothes))