class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print(self):
        cur = self.head
        cnt = 10
        while cnt > 0:
            print(cur.data, end=' ')
            cur = cur.next
            cnt -= 1

    def get_node(self, index): #index에 해당하는 노드 반환
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
    
    def append(self, data): #맨 뒤에 새로운 노드 추가
        cur = self.tail
        cur.next = Node(data)
        self.tail = cur.next
    
    def insert(self, index, data:list): #index 뒤에 새로운 노드리스트 추가
        st = 0
        if index==0:
            if self.head is not None:
                new_node = Node(data[0])
                new_node.next = self.head
                self.head = new_node
            else:
                self.head = Node(data[0])
            
            index = 1
            st = 1

        cur = self.head
        for i in range(1, index):
            cur = cur.next
        
        for i in range(st, len(data)):
            new_node = Node(data[i])
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node

        if cur.next is None:
            self.tail = cur
    
    def delete(self, index, cnt): #index 다음 cnt개의 노드를 삭제
        cur = self.head
        if index == 0:
            for i in range(cnt):
                cur = cur.next
            self.head = cur
            return

        for i in range(1, index):
            cur = cur.next
        
        anchor = cur
        
        for i in range(cnt):
            cur = cur.next
        
        anchor.next = cur.next

        if anchor.next is None:
            self.tail = anchor


for tc in range(1, 11):
    N = int(input())
    messageInput = input().split()
    message = LinkedList()
    message.insert(0, messageInput)

    M = int(input())
    for _ in range(M):
        command = input().split()
        if command[0] == 'I':
            cmd, idx, cnt, *nums = command
            message.insert(int(idx), nums)
        elif command[0] == 'D':
            cmd, idx, cnt = command
            message.delete(int(idx), int(cnt))
        elif command[0] == 'A':
            cmd, cnt, *nums = command
            for i in range(int(cnt)):
                message.append(nums[i])
    
    
    print(f'#{tc} {message.print()}')