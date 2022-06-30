from itertools import combinations

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

def solution(orders, course):
    answer = []
    length = len(orders)

    # 각 사람이 시킨 메뉴 오름차순 정렬
    for order in orders:
        order = sorted(order)

    # course의 개수만큼 씩
    for c in course:
        for i, order in enumerate(orders):
            combi = list(combinations(order, c))
            for com in combi:
                menu = ''.join(com)
                print(menu)

                # for j in range(i+1, length):
                #     if menu in orders[j] and menu not in answer:
                #         answer.append(menu)
                #         break
                
    
    return answer

print(solution(orders, course))