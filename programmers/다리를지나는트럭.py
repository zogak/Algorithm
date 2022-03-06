bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
import collections
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = collections.deque(truck_weights)
    bridge = collections.deque(maxlen = bridge_length)
 
    while truck_weights:
        answer += 1
        next = truck_weights[0]
        
        if len(bridge) == bridge_length:
            if sum(list(bridge)[1:]) + next <= weight:
                bridge.append(next)
                truck_weights.popleft()
            else:
                bridge.append(0)
        
        else:
            if sum(bridge) + next <= weight:
                bridge.append(next)
                truck_weights.popleft()
            else:
                bridge.append(0)
    answer += bridge_length
    return answer

#print(solution(bridge_length, weight, truck_weights))

def solution2(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = collections.deque(truck_weights)
    bridge = collections.deque([0]*bridge_length)
    bridge_weight = 0
    while bridge:
        answer += 1
        bridge.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer

print(solution2(bridge_length, weight, truck_weights))


def solution3(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = collections.deque(truck_weights)
    bridge = collections.deque(maxlen = bridge_length)

    total_weight = 0
    while truck_weights:
        answer += 1
        next = truck_weights[0]
        
        if len(bridge) == bridge_length:
            #if sum(list(bridge)[1:]) + next <= weight:
            if total_weight - bridge[0] + next <= weight:
                bridge.append(next)
                truck_weights.popleft()
                total_weight = total_weight - bridge[0] + next
            else:
                bridge.append(0)
        
        else:
            #if sum(bridge) + next <= weight:
            if total_weight + next <= weight:
                bridge.append(next)
                truck_weights.popleft()
                total_weight = sum(bridge)
            else:
                bridge.append(0)
    answer += bridge_length
    return answer