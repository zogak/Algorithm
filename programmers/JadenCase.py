def solution(s):
    answer = ''
    words = list(s.split())
    # 공백문자가 연속해서 나올 수 있다는 것은 s.split(" ")로 하면 안된다는 것
    
    for i, word in enumerate(words):
        if word[0].isdecimal():
            words[i] = word.lower()
        else:
            words[i] = word[0].upper() + word[1:].lower()
    
    return ' '.join(words)

print(solution("3people  unFollowed me"))