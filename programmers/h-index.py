def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    for i, citation in enumerate(citations):
        if citation >= (i+1):
            answer = i+1
    return answer