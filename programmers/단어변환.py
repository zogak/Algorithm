begin = "1234567000"
target = "1234567899"
words = ["1234567800", "1234567890", "1234567899"]

'''
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
'''
from collections import defaultdict, deque

def review(begin, target, words):
    
    def isConnected(a, b):
    # 주의할 점은 a단어와 b단어가 가지고 있는 글자가 하나만 다르냐
    # 라고 생각하지 말고,
    # 둘의 길이는 똑같으니
    # 모든 자리의 알파벳이 같아야 하며
    # 한 자리만 달라야 한다.
        count = 0
        for i, char in enumerate(a):
            if char != b[i]:
                count += 1

        if count == 1:
            return True
        return False
    print(isConnected('1234567800', '1234567890'))

    whole = words
    whole.append(begin)
    
    # words 리스트 맨 앞에 begin을 붙이고 싶었음
    # whole = [begin]
    # whole += words
    graph = defaultdict(list)

    for i in range(len(whole)-1):
        for j in range(i+1, len(whole)):
            print(whole[i], whole[j])
            if (isConnected(whole[i], whole[j])):
                print('connected')
                graph[whole[i]].append(whole[j])
                graph[whole[j]].append(whole[i])
    print('graph: ', graph)

    check = dict.fromkeys(whole, 0)

    def bfs(start):
        cnt = 0
        check[start] = 1
        q = []
        q.append(start)
        print('q : ', q)
        while q:
            q_size = len(q)
            print('q_size : ', q_size)
            for _ in range(q_size):
                v = q.pop()
                print('v : ', v)
                if v==target:
                    break
                for item in graph[v]:
                    if check[item] == 0:
                        check[item] = 1
                        q.append(item)
            cnt += 1
        return cnt
    
    return bfs(begin)-1

print(review(begin, target, words))



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

#print(solution(begin, target, words))