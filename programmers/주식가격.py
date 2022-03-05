def solution(prices):
    totalLength = len(prices) - 1
    answer = [0] * len(prices)
    stack = []
    for i, cur in enumerate(prices):
        while stack and cur < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    for item in stack:
        answer[item] = totalLength - item
    return answer