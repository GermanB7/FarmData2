from DoublyLinkList import *

class Notifications():
    def __init__(self):
        self.days = 0
        self.notificaciones = DoublyLinkedList()
        # O(1)
        
    def passDays(self):
        self.days += 1
        # O(1)
        
    def generateNotifications(self,vacas):
        print("self.days: ",self.days)                         # fr
        dayActual = self.days                                  # fd + fa
        nodo = vacas.head                                      # fd
        for i in range(vacas.count):                           # n * (fc +1)
            node = DoublyLinkedList()                          # n * (fd + 3fd + fa)  
            if nodo.next != None:                              # fc * n
                if nodo.data.FindKth(1) == "1":                # n * (5fc + fa + 2 *(fd + fr) +fr )
                    node = node.add_last(nodo.data.FindKth(0)) # n * (5fc + fa + 1 *(fd + fr) + fr + 8fd +6fa + 4fd + 2fr)
                    node = node.add_last("Vaca en gestacion, días para parto!: "+str(dayActual + int(nodo.data.FindKth(1))))  # n * (5fc + fa + 2 *(fd + fr) +fr + 8fd +6fa + 4fd + 2fr) 
                    self.notificaciones = self.notificaciones.add_last(node)  # n * (9fd +6fa + 4fd + 2fr)
                nodo = nodo.next                               # n * fa                 
        return self                                            # fr
                                                               # 10nfr + fr + 8nfd + 12fd + 25nfa + fa + 15nfc
        #O(N) O(1) O(1) O(1)                                   # O(N)
                                                              
        #O(N)   
    
    def showNotifications(self):
        print(self.notificaciones.count)
        self.notificaciones.PrintList()
        
        
        
                
        
        
    
    
    
    