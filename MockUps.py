from random import randint

class MockupData:
    def genMvacas(self,n,nombre):
        # Código - Tipo - Edad - Género - Peso - Raza - Lechera - Gestación - Día_gestación- Salud
        datos = [1,2,3,4,5,1,1,1,1,1,2,3,2,1,3,"M","H","M","M","H",800,750,780,700,720,"Angus","Angus","Angus","Angus","Angus",False,True,False,True,True,True,True,True,True,True,"Bien","Bien","Bien","Bien","Bien"]
        with open(nombre+'.txt','w') as txt:
            for x in range(n):
                ind = randint(0,4)
                dias_g = randint(2,10)
                txt.write(f"{x+1} {datos[ind+5]} {datos[ind+10]}\n")
            txt.write("fin"+str(x))
            txt.close()

    def genMpedidos(self,n,nombre):
        # Código - Nombre - Contacto - Tipo_animal - Cantidad - Peso
        datos = [1001,1002,1003,1004,1005,"Juan-Rodriguez","Pablo-Pérez","Luisa-Diaz","Marco-Meneses","Camilo-Corredor",2382957384,327482742,25464232,234563,6346436,1,1,1,1,1,10,5,4,7,15,800,750,780,700,720]
        with open(nombre+'.txt','w') as txt:
            for x in range(n):
                ind = randint(0,4)
                txt.write(f"{x+1} {datos[ind+15]} {datos[ind+20]}\n")
            txt.write("fin"+str(x))
            txt.close()