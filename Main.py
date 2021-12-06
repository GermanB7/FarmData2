from DoublyLinkList import DoublyLinkedList
from Sistematizar import Sistematizar
#from Stack import LinkedListStack
#from MockUpsV2 import MockupData 
from Notificaciones import Notifications
#from ApiladorAnimales import *
from ControlPedidos import OrderControl
from Queue import DoubleLinkedListQueue
from MockUps import MockupData

import time


def main():

    
 #Datos Array
   
    
    
    
# Datos vacas
  node = DoublyLinkedList()
  vacas = DoublyLinkedList()
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
    
  
  opM = 0
  print("Bienevido al sistema farm data")
  print(" ")
  while opM != 5:
      print("")
      
      print("1) List")
      print("2) Stacks")
      print("3) Queue")
      print("4) Generador de mokups")
      
      try:
          opM = int(input())
      except:
          print("numero invalido")
      
      if opM == 1:
          op = 0  
          print("lISTAS")
          while op != 7:
            print(" ")
            print("Escoga alguna opción")
            
            print("1) Imprimir lista")
            print("2) Limpiar Lista")
            print("3) Encontrar un elemento")
            print("4) Insertar un elemento")
            print("5) Remover un elemento")
            print("6) Encontra un k elemento")
            print("8) Insertar elemento al final")
            print("7) Salir")
            print("9) Lista de vacas")
            print("11) Cargar la lista")
            print("12) Notificaciones")
            print("13) Ver Notificaciones")
            
        
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
                
                vacas = DoublyLinkedList()
            
            elif op == 3:
                
                print("Digite la posisión de la lista")
                try:
                    posicion = int(input())
                except:
                    print("Dato invalido")
                
                print("Digite el dato a encontrar")
                try:
                    data = input()
                except:
                    print("Dato invalido")

                print(vacas.FindElement(posicion))


            elif op == 4:
                '''
                print("Digite la posición del dato a insertar")
                posicion = int(input())
                nodeaxu = ListedLinkList(None)
                nodoFinal = ListedLinkList(None) 
                print("Digite el codigo de la vaca")
                codigo = input()
                nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(codigo, nodoFinal)
                print("1 si es lechera, 0 si no")
                lechera = input()
                nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(lechera, nodoFinal)
                print("Digite el peso de la vaca")
                peso = input()
                nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(peso, nodoFinal)

                nodeaxu = node.InsertElement(posicion,nodeaxu,tamañoNotificaciones)
                if posicion <= vacasSize:
                    vacasSize += 1
                '''
                pass
                
            elif op == 5:
                print("Digite la posicion del dato a eliminar")
                try:
                    position = int(input())
                    vacas = vacas.RemoveElement(position)
                except:
                    print("Digite el dato correctamente")
                    
                
            elif op == 6:
                print("Digite la posición del elemento a encontrar")
                try:
                    k = int(input())
                    vacas.FindKth(k).printList()
                except:
                    print("Digite el dato correctamente")
            elif op == 7:
                break
        
                    
                    
            elif op == 9:
                if vacas != None:
                    data = input()
                    vacas.add_last(data)
                else:
                    print("Lista vacía carguela, opcion 11")
                    
                    
                
            elif op == 11:
                print("Cargar")
                vacas = Sistematizar.cargarDoublyLinkedList(0)
            elif op == 12:
                print("vacasSize ",vacas.count)
                
                if vacas.head != None:
                    ini = time.time()
                    notification = notification.generateNotifications(vacas)
                    print("Notificaciones generadas")
                    end = time.time() - ini
                    print("Tiempo: ",end, "Ms " )
                    a = input()                
                else:
                    print("Lista vacía")
                              
            elif op == 13:
                    notification.showNotifications()
                
            elif op == 14:
                vacas.printList()
            
            else:
                print("Opción invalida")
        
            a = input("Presione ENTER")
            
                 
      elif opM == 3:
          print("GESTIÓN DE PEDIDOS")
          op = 0  
          while op != 3:
                print(" ")
                print("Escoga alguna opción")
                
                print("1) Crear pedido")
                print("2) Ver lista de pedidos")
                print("3) Control de pedidos")
                print("4) Salir")
                print("5) Subir datos")
                print("6) Cargar datos")
            
            
                op = int(input())
                if op == 1:
                    datos = [input("Código: "), input("Tipo animal: "), input("Cantidad: ")]
                    pedido.enqueue(datos[0])
                    pedido.enqueue(datos[1])
                    pedido.enqueue(datos[2])
                    lista_pedidos.enqueue(datos)
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
                elif op == 5:
                    print("Subir")
                    Sistematizar.cargarLinkQueue(lista_pedidos,1,lista_pedidos.count)
            
                elif op == 6:
                    print("Cargando datos.....")
                    lista_pedidos = Sistematizar.cargarDoubleLinkedListQueue(1)
        
      elif opM == 4:
          op = 0
          while op != 7:
              genData = MockupData()
              print("Creación de mokups data ")
              print("")
              
              print("Escoga alguna opción")
              print("1) Generar mokup de vacas")
              print("2) Generar mokup de pedidos")  
              print("3) Salir")
              op = int(input())
              
              """try:
                  op = int(input())
              except:
                  print("ERROR DE CASTING A NUMERO")
                  op = 0
              """
              if op == 1:
                  print("Digite el tamaño del mokup 'vacas' :")
                  try:
                    tam = int(input())
                    print("Digite el nombre del archivo")
                    nombre = input()
                    genData.genMvacas(tam, nombre)
                  except:
                      print("Digite el dato correctamente")
                  
              elif op == 2:
                  print("Digite el tamaño del mokup 'pedidos' :")
                  tam = int(input())
                  print("Digite el nombre del archivo")
                  nombre = input()
                  genData.genMpedidos(tam,nombre)
              elif op == 3:
                  break
                  
                  
              else:
                  print("Opción invalida")      
                      
                  
                    
main()