import time
import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def inorder(self,root):
        if root is not None:
     
            self.inorder(root.left)
    
            # Traverse root
            print(str(root.key) + "->", end=' ')
    
            # Traverse right
            self.inorder(root.right)
    
    def insert(self, key):
        if self.key is None:
            nodo = Node(key)
            return nodo
        
        elif key < self.key:
            if self.left == None:
                self.left = Node(key)
            else:
                self.left = self.left.insert(key)
        elif key > self.key:
            if self.right == None:
                self.right = Node(key)
            else:
                self.right = self.right.insert(key)
        return self
         
    # Find the inorder successor
    def minValueNode(self,node):
        current = node
    
        # Find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
    
    # Deleting a node
    def deleteNode(self,root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif(key > root.key):
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.deleteNode(root.right, temp.key)
        return root
    
 
    def preorder(self,node):
        if node == None:
            return 
        print(node.key)
        self.preorder(node.left)
        self.preorder(node.right)
        
    def find(self,data, nodo):
        if nodo.key > data:
            if nodo.left != None:
                self.find(data,nodo.left)
        elif nodo.key < data:
            if nodo.right != None:
                self.find(data,nodo.right)
        elif nodo.key == data:
            pass
            #print(nodo.key)
        else:
            print("Dato no encontrado")
        

# node = Node(1)           
# cont = 1
# numbers = int(input())
# start = time.time()
# while numbers > cont:
#     node.insert(cont)
#     cont += 1
# end = time.time()
# print("Insercion:",end-start)
  
# cont = 0
# startTime = time.time()
# while(cont < numbers):
#     cont += 1
#     node.find(cont, node)
# endTime = time.time()
# print("Find:",endTime - startTime)


# cont = 0
# root = node
# startTime = time.time()
# while(cont < numbers):
#     cont += 1 
#     root = node.deleteNode(root, cont)
# endTime = time.time()
# print("Delete:",endTime - startTime)


# print("----------------------")
