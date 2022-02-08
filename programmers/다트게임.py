bonus = {
    "S" : 1,
    "D" : 2,
    "T" : 3
}
def solution(dartResult):
    answer = 0
    score = [0]*3
    game_round = -1
    option = ""
    isTen = False
    for i, char in enumerate(dartResult):
        if char.isdigit():
            if isTen:
                isTen = False
                continue

            if dartResult[i+1].isdigit():
                isTen = True
                
                game_round += 1
                score[game_round] = 10
            else:
                game_round += 1
                score[game_round] = char
        elif char.isalpha():
            score[game_round] = int(score[game_round]) ** bonus[char]
        else:
            option += char
            if char == '*':
                if game_round == 0:
                    score[game_round] *= 2
                else:
                    score[game_round-1] *= 2
                    score[game_round] *= 2
            elif char == '#':
                score[game_round] *= (-1)
    answer = sum(score)
    return answer