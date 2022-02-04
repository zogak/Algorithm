'''
오픈채팅방
'''
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer = []
    userInfo = dict()
    
    for r in record:
        if r.split()[0] == 'Enter':
            id, nickName = r.split()[1][3:], r.split()[2]
            # id alreay exists
            if id in userInfo:
                # same nickName
                if userInfo[id] == nickName:
                    message = id+nickName+'님이 들어왔습니다.'
                    answer.append(message)
                # new nickName
                else:
                    oldNickName = userInfo[id]
                    userInfo[id] = nickName
                    for ans in answer:
                        if ans[0:4] == id: # 숫자를 4자리로 한정
                            ans = ans.replace(oldNickName, nickName)
                    message = id+nickName+'님이 들어왔습니다.'
                    answer.append(message)
                    
            # new id
            else:
                userInfo[id] = nickName
                message = id+nickName+'님이 들어왔습니다.'
                answer.append(message)
                
        elif r.split()[0] == 'Change':
            id, nickName = r.split()[1][3:], r.split()[2]
            oldNickName = userInfo[id]
            userInfo[id] = nickName
            
            for ans in answer:
                if ans[0:4] == id: #숫자를 4자리로 한정
                    ans = ans.replace(oldNickName, nickName)
        elif r.split()[0] == 'Leave':
            id = r.split()[1][3:]
            nickName = userInfo[id]
            message = id+nickName+'님이 나갔습니다.'
            answer.append(message)
        print(userInfo)

    for ans in answer:
        id = ans[0:4] #숫자를 4자리로 한정
        ans = ans.replace(id, '')
    return answer

print(solution(record))