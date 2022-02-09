import time

class HashMap_DA:
    def __init__(self,n):
        self.n_el = 0
        self.N = n
        self.r = self.PreviousPrime(n)
        self.table = [[None,None]] * self.N
    
    def NextPrime(self, n):
        if (n % 2 == 0 and n != 2):
            n += 1
        while(not self.isPrime(n)):
            n += 2
        return n

    def PreviousPrime(self,n):
        if n >= 3:
            if (n % 2 == 0):
                n -= 1
            else:
                n -= 2
        while(not self.isPrime(n)):
            n -= 2
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
    

    # Función hash
    def Hash_func(self, value, i):
        try:
            h2 = self.r - (value % self.r)
            f = i * h2
            return (value + f) % self.N
        except:
            raise Exception("Hashing Error")

    def rehashing(self):
        n = self.N
        copy = HashMap_DA(n*2)
        for d in self.table:
            if d[0] != None:
                copy.Insert(d[0],d[1])
        self.n_el = copy.n_el
        self.N = copy.N
        self.r = copy.r
        self.table = copy.table

    def Insert(self, llave, valor): # Metodo para ingresar elementos
        i = 0
        while True:
            hash = self.Hash_func(llave,i)
            if self.table[hash][0] is None:
                self.table[hash] = [llave,valor]
                self.n_el += 1
                break
            else:
                if self.table[hash][0] == llave:
                    self.table[hash][1] = valor
                    break
                else:
                    i += 1

        if (self.n_el/self.N) > 0.5:
            self.rehashing()

    def PrintHash(self):
        for d in range(self.N):
            print(f"{d} -> {self.table[d]}")

    def Search(self,llave): # Metodo para buscar elementos
        i = 0
        while True:
            hash = self.Hash_func(llave,i)
            if self.table[hash][0] is None:
                return None
            elif self.table[hash][0] == llave:
                return self.table[hash]
            else:
                i += 1
  
    def Delete(self,llave): # Metodo para eleminar elementos
        i = 0
        while True:
            hash = self.Hash_func(llave,i)
            if self.table[hash][0] is None:
                #print("No hay elementos con ese valor", llave)
                return
            elif self.table[hash][0] == llave:
                self.table[hash] = [None,None]
                self.n_el -= 1
                #print("Elemento con valor", llave, "eliminado")
                return
            else:
                i += 1
  

def main():
    t = HashMap_DA(3)
    while True:
        op = int(input("Escoga:\n1) Imprimir tabla\n2) Insertar\n3) Buscar\n4) Eliminar\n"))
        if op == 1:
            t.PrintHash()
        elif op == 2:
            t.Insert(int(input("Llave: ")),input("Valor: "))
        elif op == 3:
            elem = t.Search(int(input("Ingrese la llave a buscar: ")))
            print(elem)
        elif op == 4:
            t.Delete(int(input("Ingrese la llave a eliminar: ")))
        
def main2():
    t = HashMap_DA(20000005)

    archivo = "Animales10k.txt"

    with open(archivo, 'r') as txt:
        ini = time.time()
        while True:
            linea = txt.readline()
            if linea[:3] == "fin":
                break
            else:
                try:
                    datos = linea[:-1].strip().split(" ")
                    t.Insert(int(datos[0]),datos[1])
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
                    print("No se pudo cargar los datos.")
    end = time.time() - ini
    print("Tiempo Eliminación: ",end, "Ms " )
                    

main2()