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
                head.data.PrintList()
                head = head.next
            head.data.PrintList()

    def enqueue(self, data):
        if self.head is None:               # fc
            node = Node(data)               # fd 
            self.head = node
            self.tail = node
            self.count += 1
            return
        node = Node(data)
        self.tail.next = node
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
            
def mainQueue():
    cola = DoubleLinkedListQueue()
    datos = int(input())
    ini = time.time()
    for i in range(datos):
        cola.enqueue(i+1)
    end = time.time() - ini
    print("Tiempo Enqueu: ",end, "Ms " )


    ini = time.time()
    tiempo1 = 0
    tiempo2 = 0
    for i in range(datos):
        t = time.time()
        cola.Peek()
        tiempo1 += time.time()-t
        t = time.time()
        cola.dequeue()
        tiempo2 += time.time()-t
    end = time.time() - ini
    print("Tiempo Peek: ",tiempo1, "Ms " )
    print("Tiempo Dequeue: ",tiempo2, "Ms " )

#mainQueue()