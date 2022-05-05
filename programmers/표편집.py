'''
list 사용하여 구현
정확도 테스트 통과, 효율성 미통과
'''
def solution(n, k, cmd):
    answer = ''
    origin_length = n
    delete_log = []
    table = [x for x in range(n)]
    for item in cmd:
        if item[0] == "U":
            x = int(item[2:])
            k = (k-x) % n
        elif item[0] == "D":
            x = int(item[2:])
            k = (k+x) % n
        elif item == "C":
            max_idx_before_remove = len(table)-1
            delete_log.append((k, table[k]))
            table.remove(table[k])
            #마지막거 지우면
            if k==max_idx_before_remove:
                k = k-1
            n = n-1
        elif item == "Z":
            index, value = delete_log.pop()
            table.insert(index, value)
            if index <= k:
                k = k+1
            n = n+1
        
        print("--------------------")
        print(table)
        print("cursor   ", k)
        print("log   ", delete_log)
        print("--------------------")

    print("table   ", table)
    print("log   ", delete_log)        
    res = ["O"]*origin_length
    for log in delete_log:
        res[log[1]] = "X"
    answer = ''.join(res)
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#print(solution(n, k, cmd))

'''
linked list 사용
'''

class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.removed = False
        
def solution2(n, k, cmd):
    answer = ''
    linked_list = [Node() for _ in range(n)]
    for i in range(1, n-1):
        linked_list[i].prev = linked_list[i-1]
        linked_list[i].next = linked_list[i+1]
    
    stack = []
    cur = k
    for item in cmd:
        if item[0] == "U":
            for i in range(int(item[2:])):
                cur = linked_list[cur].prev
        elif item[0] == "D":
            for i in range(int(item[2:])):
                cur = linked_list[cur].next
        
        elif item == "C":
            linked_list[cur].removed = True
            stack.append(cur)

            prev = linked_list[cur].prev
            next = linked_list[cur].next

            if prev == None:
                linked_list[next].prev = None
                linked_list[cur].next = None
            elif next == None:
                linked_list[prev].next = None
                linked_list[next].prev = None
            else:
                linked_list[prev].next = linked_list[next]
                linked_list[next].prev = linked_list[prev]
        
        elif item == "Z":
            pass
    return answer

print(solution2(n, k, cmd))