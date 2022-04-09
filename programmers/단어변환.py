begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
def solution(begin, target, words):
    if target not in words:
        return 0
    word_length = len(begin)
    answer = 0
    road = dict()
    def isConnected(a, b):
        if len([char for char in a if char not in b])==1:
            return True
        return False
    
    whole = [begin]
    whole += words
    for i in range(len(whole)):
        for j in range(len(whole)):
            cur = whole[i]
            next = whole[j]
            if cur==next:
                continue
            if cur not in road:
                road[cur] = list()
            if isConnected(cur, next):
                road[cur].append(next)
    #print(road)
    def bfs(begin, answer):
        check[begin] = 1
        q = [begin]
        while q:
            answer += 1
            v = q.pop()
            if v == target:
                break
            for item in road[v]:
                if check[item]==0:
                    check[item] = 1
                    q.append(item)
        return answer

    check = dict.fromkeys(whole, 0)
    answer = bfs(begin, answer) - 1
    
    return answer

print(solution(begin, target, words))