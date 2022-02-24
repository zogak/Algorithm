genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 500, 800, 2500]

import collections
def solution(genres, plays):
    answer = []

    info = zip(range(len(genres)), genres, plays)
    info = list(map(list, info))
    #print(info)

    sortOfGenre = list(set(genres))
    #print(sortOfGenre)
    playsByGenre = collections.defaultdict(int)
    for item in info:
        playsByGenre[item[1]] += item[2]
    #print(playsByGenre)
    sortedGenre = list(map(list, playsByGenre.items()))
    sortedGenre.sort(key = lambda x : -x[1])
    #print(sortedGenre)

    genreToNum = dict()
    for item in sortedGenre:
        genreToNum[item[0]] = sortedGenre.index(item)
    #print(genreToNum)

    for item in info:
        item[1] = genreToNum[item[1]]
    #print(info)
    info.sort(key = lambda x : (x[1], -x[2], x[0]))
    #print(info)

    check = dict.fromkeys(genreToNum.values(), 0)
    #print(check)

    for item in info:
        if check[item[1]] == 2:
            continue
        answer.append(item[0])
        check[item[1]] += 1
    return answer

print(solution(genres, plays))