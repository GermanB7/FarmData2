from DoublyLinkList import *
from Queue import DoubleLinkedListQueue
class Sistematizar():
    global lista_archivos
    lista_archivos = [
        'Mokup Data\\vacas10000.txt',
        'Mokup Data\\pedidos10000.txt']

    def cargarDoublyLinkedList(arch):
        global lista_archivos
        lista_c = DoublyLinkedList()
        with open(lista_archivos[arch], 'r') as txt:
            while True:
                linea = txt.readline()
                if linea == "":
                    break
                else:
                    try:
                        datos = linea[:-1].strip().split(" ")
                        lista_datos = DoublyLinkedList()
                        for d in datos:
                            lista_datos = lista_datos.add_last(d)

                    except:
                        print("No se pudo cargar los datos.")
                lista_c = lista_c.add_last(lista_datos)
        return lista_c

    def subirLinkList(lista, arch, size):
        global lista_archivos
        with open(lista_archivos[arch], 'w') as txt:
            for i in range(size):
                for j in range(3):
                    txt.write(lista.FindKth(i).FindKth(j) + " ")
                txt.write("\n")
        print("Archivo subido correctamente.")

    def cargarDoubleLinkedListQueue(arch):
        global lista_archivos
        lista_c = DoubleLinkedListQueue()
        with open(lista_archivos[arch], 'r') as txt:
            while True:
                linea = txt.readline()
                if linea == "":
                    break
                else:
                    try:
                        datos = linea[:-1].strip().split(" ")
                        lista_datos = DoublyLinkedList()
                        for d in datos:
                            lista_datos = lista_datos.add_last(d)
                    except:
                        print("No se pudo cargar los datos.")
                lista_c = lista_c.add_last(lista_datos)
        return lista_c

    def subirLinkQueue(lista, arch):
        global lista_archivos
        with open(lista_archivos[arch], 'w') as txt:
            for i in range(lista.lenght()):
                for j in range(lista.FindKth(i).getSize()):
                    txt.write(lista.FindKth(i).FindKth(j) + " ")
                txt.write("\n")
        print("Archivo subido correctamente.")

    def cargarLinkStack(arch):
        global lista_archivos
        lista_c = DoublyLinkedList(None)
        with open(lista_archivos[arch], 'r') as txt:
            while True:
                linea = txt.readline()
                if linea == "":
                    break
                else:
                    try:
                        datos = linea[:-1].strip().split(" ")
                        lista_datos = DoublyLinkedList(None)
                        for d in datos:
                            lista_datos = lista_datos.Push(d)
                    except:
                        print("No se pudo cargar los datos.")
                lista_c = lista_c.Push(lista_datos)
        return lista_c

    def subirLinkStack(lista, arch, size):
        global lista_archivos
        with open(lista_archivos[arch], 'w') as txt:
            for i in range(size):
                for j in range(2):
                    txt.write(lista.FindKth(size - 1 - i).FindKth(1 - j) + " ")
                txt.write("\n")
        print("Archivo subido correctamente.")

