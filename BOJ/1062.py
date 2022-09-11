import sys
from itertools import combinations

input = sys.stdin.readline

def solution():

    def countReadableWords(words, learned):
        cnt = 0
        for word in words:
            readable = True
            for w in word:
                if learned[ord(w)] == 0:
                    readable = False
                    break
            
            if readable:
                cnt += 1

        return cnt


    n, k = map(int, input().split())

    basic = {'a', 'c', 'i', 'n', 't'}
    alphabets = set(chr(i) for i in range(97, 123)) - basic

    ans = 0
    words = []
    for _ in range(n):
        word = input().rstrip()[4:-4]
        words.append(word)

    if k < 5:
        print("0")
        return

    else:
        learned = [0]*123

        # 5가지 알파벳 안다고 체크
        for b in basic:
            learned[ord(b)] = 1

        # 주어진 word를 기준으로 하는 것이 아니라,
        # 배울 단어 조합을 만들어 놓고 그것을 기준으로
        combi = list(combinations(alphabets, k-5))
        
        cnt = 0
        for com in combi:
            for c in com:
                learned[ord(c)] = 1
            readable = countReadableWords(words, learned)

            if readable >= cnt:
                cnt = readable
            
            for c in com:
                learned[ord(c)] = 0
        
        print(cnt)
        return

solution()