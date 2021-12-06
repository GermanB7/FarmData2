from DoublyLinkList import *

class DoubleLinkedListQueue(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def printQueue(self):
        if self.head == None:
            print("Cola vacía")
            return 
        head = self.head
        if type(head.data) != DoubleLinkedListQueue and type(head.data) != DoublyLinkedList:
            while head.next != None:
                print(head.data, end = " ")
                head = head.next
            print(head.data)
        else:
            while head.next != None:
                head.data.printQueue()
                head = head.next
            head.data.printQueue()

    def enqueue(self, data):
        if self.head is None:               # fc
            node = Node(data)               # fd 
            self.head = node
            return

        node = Node(data)
        node.prev = self.tail
        self.tail = node
        self.count += 1

    def dequeue(self):
        if self.head is None:
            print("Cola vacía")
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.count -= 1
            return
        self.head = self.head.next
        self.count -= 1

    def MakeEmpty(self):
        return super().MakeEmpty()

    def Peek(self):
        if self.head != None:
            return self.head.data
        else:
            print("Cola vacía")
            return None

    def Lower(self):
        if self.tail != None:
            return self.tail.data
        else:
            print("Cola vacía")
            