def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, int(total**0.5)+1):
        h = i
        if total%h != 0:
            continue
        w = total//h
        if (h-2)*(w-2) == yellow:
            answer = [w, h]
    return answer