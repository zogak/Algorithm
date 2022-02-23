genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
orderOfGenres = []

from functools import cmp_to_key
import collections
def orderByGenre(x, y):
    return orderOfGenres.index(x[1]) - orderOfGenres.index(y[1])

def solution(genres, plays):
    answer = []
    musicNums = []
    for i in range(len(genres)):
        musicNums.append(i)
    info = list(zip(musicNums, genres, plays))
    info.sort(key = lambda x : -x[2])

    numOfGenres = len(set(genres))
    
    for i in info:
        if len(orderOfGenres) == numOfGenres:
            break
        if i[1] not in orderOfGenres:
            orderOfGenres.append(i[1])
    
    check = dict(collections.Counter(orderOfGenres))
    info = sorted(info, key = cmp_to_key(orderByGenre))
    
    for i in info:
        if check[i[1]] >= 3:
            continue
        answer.append(i[0])
        check[i[1]] += 1
    
    return answer
    
print(solution(genres, plays))