from Queue import DoubleLinkedListQueue

class OrderControl:
    def __init__(self):
        self.lista_pedidos = DoubleLinkedListQueue()
        self.dias = 0
        self.diasAcum = 0

    def passDays(self):
        self.dias += 1                                    # fa + fo
        self.diasAcum += 1                                # fa + fo 
                                                          # B
                                                          # O(1)
                                                          
    def mostrarPedidos(self):            
        self.lista_pedidos.printQueue()                


    def guardarPedido(self,lista_datos):
        pedido = lista_datos.head                         # fa + fb
        while pedido.next != None:                        # n * fc
            self.lista_pedidos.enqueue(pedido.data)       # n * 3(fd + fa)
            pedido = pedido.next                          # n * fd     
        return self                                       # fr  
                                                          # 3nfa + fa + nfc + 3nfd + fr
                                                          # A + n * B
                                                          # O(N)
                                                          
    

# def main2():
#     # Funcionalidad como tal
#     pedidos = OrderControl()
#     with open("archivo",'r') as txt:
#         while True:
#             linea = txt.readline()
#             if linea == "":
#                 break
#             else:
#                 try:
#                     # Código - Tipo_animal - Cantidad
#                     datos = linea[:-1].strip().split(" ")
#                     pedidos.guardarPedido(datos)
#                 except:
#                     print("No se pudo cargar los datos.")
           
#     pedidos.mostrarPedidos()
