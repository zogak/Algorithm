import collections
cacheSize = 2
cities = 	["Jeju", "Pangyo", "NewYork", "newyork"]
import collections
def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque()
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()

            if len(cache) < cacheSize:
                if city in cache:
                    cache.remove(city)
                    cache.append(city)
                    answer += 1
                else:
                    cache.append(city)
                    answer += 5
            else:
                if city in cache:
                    cache.remove(city)
                    cache.append(city)
                    answer += 1
                else:
                    cache.popleft()
                    cache.append(city)
                    answer += 5
                
    return answer
print(solution(cacheSize, cities))



def solution2(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen = cacheSize)
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()

            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                answer += 5
    return answer