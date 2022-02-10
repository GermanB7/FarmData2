from cmath import pi
import time

#separate chaining in python
class Node() :
    def __init__(self,value) :
        self.value = value
        self.next = None

class Linked_List() :
    
    def __init__(self) :
        self.head = None
        
    def insert(self,value) :
        if not self.head :
            self.head = Node(value)
        else :
            temp = self.head
            if temp.value[0] == value[0]:
                temp.value[1] = value[1]
                return
            while temp.next :
                temp = temp.next
                if temp.value[0] == value[0]:
                    temp.value[1] == value[1]
                    return
            temp.next = Node(value)
            
    def search(self,value) :
        temp = self.head
        while temp :
            if temp.value[0] == value :
                return temp.value
            temp = temp.next
        return None

    def delete(self,value) :
        temp = self.head
        if temp != None:
            if temp.value[0] == value:
                self.head = temp.next
                return True

        while temp.next :
            if temp.next.value[0] == value:
                temp.next = temp.next.next
                return True
            temp = temp.next
            
        return False
    
    def iterar(self):
        actual = self.head
        while actual:
            dato = actual.value
            actual = actual.next
            yield dato

    def print_LL(self) :
        temp = self.head
        if not temp :
            print(None)
        while temp :
            if temp.next :
                print(temp.value,"--->",end="  ")
            else :
                print(temp.value)
            temp = temp.next
            
            
class HashMap_DC() :
    def __init__(self,size) :
        self.n_el = 0
        self.N = self.NextPrime(size)
        self.hashtable = [None]*self.N
        
    def NextPrime(self, n):
        if (n % 2 == 0 and n != 2):
            n += 1
        while(not self.isPrime(n)):
            n += 2
        return n

    def isPrime(self, n):
        if( n == 2 or n == 3 ):
            return True
        if( n == 1 or n % 2 == 0 ):
            return False
        for i in range(3,n,2):
            if( n % i == 0 ):
                return False
        return True
    
    def hash(self,key) :
        # Hash function is h(x) = x % N
        return key % self.N
    
    def rehashing(self):
        n = self.N
        copy = HashMap_DC(n*2)
        for d in self.hashtable:
            if d != None:
                for par in d.iterar():
                    if par[0] != None:
                        copy.Insert(par[0],par[1])
        self.n_el = copy.n_el
        self.N = copy.N
        self.hashtable = copy.hashtable

    def Insert(self,key,value):
        index = self.hash(key)
        if self.hashtable[index] == None:
            self.hashtable[index] = Linked_List()
        self.hashtable[index].insert([key,value])
        self.n_el += 1
        
        # if (self.n_el/self.N) > 1:
        #     self.rehashing()
        
    def Search(self,key):
        index = self.hash(key)
        return self.hashtable[index].search(key)

    def Delete(self,key):
        index = self.hash(key)
        if (self.hashtable[index].delete(key)):
            self.n_el -= 1

    
    def print_HT(self):
        for x in range(self.N) :
            print(x,end="   ")
            self.hashtable[x].print_LL()
    

def main():
    t = HashMap_DC(3)
    while True:
        op = int(input("Escoga:\n1) Imprimir tabla\n2) Insertar\n3) Buscar\n4) Eliminar\n"))
        if op == 1:
            t.print_HT()
        elif op == 2:
            t.Insert(int(input("Llave: ")),input("Valor: "))
        elif op == 3:
            elem = t.Search(int(input("Ingrese la llave a buscar: ")))
            print(elem)
        elif op == 4:
            t.Delete(int(input("Ingrese la llave a eliminar: ")))

def main2():
    t = HashMap_DC(10000000)

    archivo = "Animales10000k.txt"

    with open(archivo, 'r') as txt:
        c = 0
        ini = time.time()
        while True:
            linea = txt.readline()
            if linea[:3] == "fin":
                break
            else:
                try:
                    datos = linea[:-1].strip().split(" ")
                    t.Insert(int(datos[0]),datos[1])
                    print(c)
                    c += 1
                except:
                    print("No se pudo cargar los datos.")
    end = time.time() - ini
    print("Tiempo Inserción: ",end, "Ms " )

    print(t.n_el/t.N)

    with open(archivo, 'r') as txt:
        ini = time.time()
        while True:
            linea = txt.readline()
            if linea[:3] == "fin":
                break
            else:
                try:
                    datos = linea[:-1].strip().split(" ")
                    x = t.Search(int(datos[0]))
                except:
                    print("No se pudo cargar los datos.")
    end = time.time() - ini
    print("Tiempo Búsqueda: ",end, "Ms " )

    with open(archivo, 'r') as txt:
        ini = time.time()
        while True:
            linea = txt.readline()
            if linea[:3] == "fin":
                break
            else:
                try:
                    datos = linea[:-1].strip().split(" ")
                    t.Delete(int(datos[0]))
                except:
                    pass
    end = time.time() - ini
    print("Tiempo Eliminación: ",end, "Ms " )
        

#main2()