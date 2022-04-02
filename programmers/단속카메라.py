def solution(routes):
    answer = 0
    # "나간 지점"을 기준으로 정렬
    routes.sort(key = lambda x : x[1])
    cam = -30001
    for route in routes:
        if route[0] > cam:
            cam = route[1]
            answer += 1
    return answer