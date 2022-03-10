operations = ["I 16", "D 1"]
import heapq
def solution(operations):
    answer = []
    heap = []
    max_heap = []
    for operation in operations:
        input = operation.split()
        order, num = input[0], int(input[1])
        if order == "I":
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-num, num))
        elif order == "D":
            if len(heap) == 0:
                pass
            elif num == 1:
                max_val = heapq.heappop(max_heap)[1]
                heap.remove(max_val)
            elif num == -1:
                min_val = heapq.heappop(heap)
                max_heap.remove((-min_val, min_val))
    
    if len(heap) == 0:
        return [0,0]
    else:
        answer.append(heapq.heappop(max_heap)[1])
        answer.append(heapq.heappop(heap))
            
    return answer

print(solution(operations))