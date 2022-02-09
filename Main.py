from DoublyLinkList import DoublyLinkedList
from Sistematizar import Sistematizar
#from Stack import LinkedListStack
#from MockUpsV2 import MockupData 
from Notificaciones import Notifications
#from ApiladorAnimales import *
from ControlPedidos import OrderControl
from Queue import DoubleLinkedListQueue
from MockUps import MockupData
from AVL import AVLTree, TreeNode
from TablaHash_DA import HashMap_DA

import time


def main():

    
 #Datos Array
    
# Datos vacas
    node = DoublyLinkedList()
    vacas = DoublyLinkedList()
    animales = DoublyLinkedList()
#   vacasFinal = ListedLinkList(None)
#   vacasFinalMatrix = ListedLinkList(None)
  
# Datos Notificaciones
    notification = Notifications()
    tamañoNotificaciones = 0

# Datos pedidos
    lista_pedidos = DoubleLinkedListQueue()
    pedidos_guardados = OrderControl()
    pedido = DoubleLinkedListQueue()

  
# Animales Apilados
#   camionesVacas = CamionesVacas()
#   nodeStack = LinkedListStack(None)
#   pedidosVacas = LinkedListStack(None)
    Caux = 0
    Ccont = 0
        
# Arbol Genealogico
    avl = AVLTree()
    root = None
    paths1 = []
    paths2 = [] 

# Hash
    t = HashMap_DA(10)


    opM = 0
    print("Bienevido al sistema farm data")
    print(" ")
    while opM != 5:
        print("")
        
        print("1) List - Notificaciones")
        print("2) Queue - Gestión de pedidos")
        print("3) AVL - Árbol genealógico")
        print("4) Hash Map (DA) - Gestión de animales")
        
        try:
            opM = int(input())
        except:
            print("numero invalido")
        
        if opM == 1:
            op = 0  
            print("LISTAS - NOTIFICACIONES")
            while op != 7:
                print(" ")
                print("Escoga alguna opción")
                print("     Listas")
                print("1) Imprimir lista")
                print("2) Limpiar Lista")
                print("3) Encontrar un elemento")
                print("4) Insertar un elemento en la lista")
                print("5) Remover un elemento")
                print("6) Encontra un k elemento")
                print("     Notificaciones")
                print("7) Notificaciones")
                print("8) Ver Notificaciones")
                
                print("9) Salir")
                
            
                try:
                    op = int(input())
                except:
                    print("Dato invalido")
                
                
                if op == 1:
                    if vacas != None:
                        vacas.PrintList()
                    else:
                        print("Lista vacas vacía")
                        
                elif op == 2:
                    vacas.MakeEmpty()
                
                elif op == 3:
                    data = input("Digite el dato a encontrar: ")
                    print(vacas.FindElement(data))


                elif op == 4:
                    print("Digite la posición del dato a insertar")
                    posicion = int(input())
                    print("Digite el dato a insertar")
                    dato = input()
                    
                    val = vacas.insert_node(posicion, dato)
                    if val == False:
                        print("Dato no insertado")
                    else:
                        print("Dato insertado")

                    
                elif op == 5:
                    node = DoublyLinkedList()
                    print("Digite la posición del dato a insertar")
                    posicion = int(input())
                    print("Digite el codigo de la vaca")
                    codigo = input()
                    node = node.add_last(codigo)
                    print("1 si es lechera, 0 si no")
                    lechera = input()
                    node = node.add_last(codigo)
                    print("Digite el peso de la vaca")
                    peso = input()
                    node = node.add_last(peso)

                    val = animales.insert_node(posicion, node)
                    
                    if val == False:
                        print("Animal no insertado")
                    else:
                        print("Animal insertado")

    #######################################################
                elif op == 5:
                    print("Digite la posicion del dato a eliminar")
                    try:
                        position = int(input())
                        vacas = vacas.RemoveElement(position)
                    except:
                        print("Digite el dato correctamente")
    #########################################################
                    
                elif op == 6:
                    print("Digite la posición del elemento a encontrar")
                    try:
                        k = int(input())
                        print(vacas.FindKth(k))
                    except:
                        print("Digite el dato correctamente")
                
                elif op == 7:
                    node = DoublyLinkedList()
                    print("Para generar notificaciones, se adiciona un animal a la lista:")

                    print("Digite el codigo de la vaca")
                    codigo = input()
                    node = node.add_last(codigo)
                    print("1 si es lechera, 0 si no")
                    lechera = input()
                    node = node.add_last(codigo)
                    print("Digite el peso de la vaca")
                    peso = input()
                    node = node.add_last(peso)

                    val = animales.add_last(node)
                    
                    if val == False:
                        print("Animal no insertado")
                    else:
                        print("Animal insertado")
                    
                    if vacas.head != None:
                        ini = time.time()
                        notification = notification.generateNotifications(vacas)
                        print("Notificaciones generadas")
                        end = time.time() - ini
                        print("Tiempo: ",end, "Ms " )
                        a = input()                
                    else:
                        print("Lista vacía")
                                
                elif op == 8:
                    notification.showNotifications()
                
                elif op == 9:
                    break
                else:
                    print("Opción invalida")
            
                a = input("Presione ENTER")
                        
        elif opM == 2:
            print("QUEUE - GESTIÓN DE PEDIDOS")
            op = 0  
            while op != 3:
                    print(" ")
                    print("Escoga alguna opción")
                    
                    print("1) Crear pedido")
                    print("2) Ver lista de pedidos")
                    print("3) Control de pedidos")
                    print("4) Salir")
                
                
                    op = int(input())
                    if op == 1:
                        pedido = DoubleLinkedListQueue()
                        datos = [input("Código: "), input("Tipo animal: "), input("Cantidad: ")]
                        pedido.enqueue(datos[0])
                        pedido.enqueue(datos[1])
                        pedido.enqueue(datos[2])
                        lista_pedidos.enqueue(pedido)
                    elif op == 2:
                        lista_pedidos.printQueue()
                        
                    elif op == 3:
                        start = time.time()
                        pedidos_guardados.passDays()                               # B
                        if pedidos_guardados.diasAcum > 0:                         # fc
                            pedidos_guardados.guardarPedido(lista_pedidos)         # A + n * B          
                            lista_pedidos = DoubleLinkedListQueue()                # fa + 3(fd + fa)
                            pedidos_guardados.diasAcum = 0                         # fa  
                                                                                # A + B + fc + nB + 3fd + 5fa
                                                                                # A + n * B
                        end = time.time() - start                                         
                        print(end, "ms ")
                            
                    elif op == 4:
                        break
                    
        elif opM == 3:
            op = 0
            
            while op != 5:
                print("Arbol genealógico ")
                print("")
                
                print("Escoga alguna opción")
                print("1) Insertar Animal")
                print("2) Mostrar Animales")  
                print("3) Eliminar Animal")
                print("4) Encontrar relación")
                print("5) Salir")
                    
                op = int(input())
                
                if op == 1:
                    
                    print("Datos a insertar")
                    datosNum = int(input())
                    cont = 0
                    
                    startTime = time.time()
                    while(cont < datosNum):
                        cont += 1 
                        root = avl.insert_node(root, cont)
                    endTime = time.time()
                    print(endTime - startTime)
    
                elif op == 2:
                    avl.preOrder(root)
                    
                elif op == 3:

                    cont = 0
                    startTime = time.time()
                    while(cont < datosNum):
                        cont += 1 
                        root = avl.delete_node(root, cont)
                    endTime = time.time()
                    print(endTime - startTime)
                    
                elif op == 4:
                    startTime = time.time()
                    paths1 = avl.FindPatch(root, 1,paths1)
                    paths2 = avl.FindPatch(root, cont,paths2)
                    repeated = ""
                    stop = False

                        
                    for k in range((len(paths1)-1),-1,-1):
                        for w in range((len(paths2)-1),-1,-1):
                            if paths1[k] == paths2[w] and stop == False:
                                repeated = paths2[w]
                                stop = True
                                break
                    
                        
                    endTime = time.time()
                    
                    for i in range((len(paths1)-1), -1,-1):
                        if paths1[i] != repeated:
                            print(paths1[i],end= ",")
                        else:
                            break
                                
                    show = False     
                    for i in range(len(paths2)):
                            
                        if paths2[i] == repeated or show:
                            show = True
                            if i != len(paths2)-1:
                                print(paths2[i], end = ",")
                            else:
                                print(paths2[i], end = "")
                                    
                    print(repeated)                
                    print(endTime - startTime)                  
                    

                elif op == 5:
                    break
                
        elif opM == 4:
            print("HASHMAP (DA) - GESTIÓN DE ANIMALES")
            while True:
                op = int(input("Escoga:\n1) Imprimir tabla\n2) Insertar\n3) Buscar\n4) Eliminar\n"))
                if op == 1:
                    t.PrintHash()
                elif op == 2:
                    t.Insert(int(input("Código: ")),input("Raza: "))
                elif op == 3:
                    elem = t.Search(int(input("Ingrese el código del animal a buscar: ")))
                    print(elem)
                elif op == 4:
                    t.Delete(int(input("Ingrese el código del animal a eliminar: ")))
            
                            
main()