def solution(ingredient):
    answer = 0
    ingredient = ''.join(map(str,ingredient))
    hamburger = '1231'
    
    while hamburger in ingredient:
        answer += 1
        ingredient = ingredient.replace(hamburger, '')
    return answer


