def solution(s, n):
    lower_z = ord("z")
    upper_z = ord("Z")
    
    answer = ''
    for alphabet in s:
        if alphabet == " ":
            answer += " "
        else:
            isLower = alphabet.islower()
            pushed_num = ord(alphabet)+n
            if isLower and pushed_num > lower_z:
                pushed_num -= 26
            elif not isLower and pushed_num > upper_z:
                pushed_num -= 26
            
            answer += chr(pushed_num)
    return answer