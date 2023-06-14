class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None) #더미 노드
        self.tail = self.head
        self.cursor = self.head

    def print(self):
        cur = self.head.next
        while cur is not None:
            print(cur.data, end='')
            cur = cur.next
        
    def getNewNode(self, data):
        return Node(data)
    
    def moveLeft(self):
        cursor = self.cursor

        if cursor != self.head:
            self.cursor = cursor.prev

    def moveRight(self):
        cursor = self.cursor

        if cursor != self.tail:
            self.cursor = cursor.next

    def delete(self):
        cursor = self.cursor
        if cursor == self.head: return

        if cursor == self.tail: #맨 뒤 삭제
            self.cursor = self.cursor.prev
            self.cursor.next = None

            self.tail = self.cursor

        else:
            prev = cursor.prev
            next = cursor.next

            self.cursor = self.cursor.prev
            prev.next = next
            next.prev = prev

    def insert(self, data):
        newNode = self.getNewNode(data)

        if self.cursor == self.tail: #맨 마지막에 추가
            self.tail.next = newNode
            newNode.prev = self.tail

            self.tail = newNode #테일 업데이트

        else:
            newNode.next = self.cursor.next
            self.cursor.next.prev = newNode
            self.cursor.next = newNode
            newNode.prev = self.cursor

        self.cursor = newNode

sentence = input()
editor = DoublyLinkedList()

for item in sentence:
    editor.insert(item)

M = int(input())
for _ in range(M):
    command = input().split()
    if command[0] == 'L':
        editor.moveLeft()
    elif command[0] == 'D':
        editor.moveRight()
    elif command[0] == 'B':
        editor.delete()
    elif command[0] == 'P':
        editor.insert(command[1])

    # editor.print()
    # print()
    # print(f'커서 위치 : {editor.cursor.data}')

editor.print()