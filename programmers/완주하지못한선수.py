participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
import collections
# def solution(participant, completion):
#     answer = ''
#     participants = collections.Counter(participant)
#     for c in completion:
#         if c in participants:
#             participants[c] -= 1
#     print(participants)
#     for p in participants:
#         if participants[p] == 1:
#             answer = p
#             break
#     return answer
# print(solution(participant, completion))

def solution(participant, completion):
    answer = ''
    running = collections.Counter(participant) - collections.Counter(completion)
    return list((running.keys()))[0]

print(solution(participant, completion))