class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.cursor = self.head
        self.tail = self.head

    def getNewNode(self, data):
        return Node(data)
    
    def print(self):
        cur = self.head.next
        while cur is not None:
            print(cur.data, end ='')
            cur = cur.next

    def moveLeft(self):
        if self.cursor == self.head : return #커서가 맨 앞에 존재
        
        self.cursor = self.cursor.prev

    def moveRight(self):
        if self.cursor == self.tail : return #커서 맨 마지막 존재

        self.cursor = self.cursor.next

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

    def delete(self):
        if self.cursor == self.head : return

        if self.cursor == self.tail:
            self.cursor = self.cursor.prev
            self.cursor.next = None
            
            self.tail = self.cursor
        
        else:
            prev = self.cursor.prev
            next = self.cursor.next

            self.cursor = self.cursor.prev

            prev.next = next
            next.prev = prev

T = int(input())
for tc in range(1, T+1):
    keylogger = DoublyLinkedList()
    password = input()

    for word in password:
        if word == '<':
            keylogger.moveLeft()
        elif word == '>':
            keylogger.moveRight()
        elif word == '-':
            keylogger.delete()
        else:
            keylogger.insert(word)

    keylogger.print()


'''
def moveCursor(dir, cursorPos, endPos):
    if dir == '<':
        if cursorPos > -1: cursorPos -= 1
    elif dir == '>':
        if cursorPos < endPos : cursorPos += 1

    return cursorPos


T = int(input())
for tc in range(1, T+1):
    cursorPos = -1 #해당 인덱스의 숫자 뒤에 위치
    res = ''
    inputTxt = input()
    for txt in inputTxt:
        if txt == '<' or txt == '>':
            cursorPos = moveCursor(txt, cursorPos, len(res)-1)
        elif txt == '-' and res[cursorPos]:
            res = res.replace(res[cursorPos], '')
        else:
            if cursorPos < 0 : res += txt
            else:
                res = res.replace(res[cursorPos], res[cursorPos]+txt) #안되는 이유: 해당 알파벳이 가장 처음에 나오는 곳을 바꿔버림.
            cursorPos += 1

        print(res)

    print(res)
'''