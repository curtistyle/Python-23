import os

class Agenda:
    def __init__(self) -> None:
        self.contactos = []                  
        
    def menu(self):
        menu = [
            ["Agenda Personal: "],
            ["1 - Añadir Contacto"],
            ["2 - Lista de Contactos"],
            ["3 - Buscar Contacto"],
            ["4 - Editar Contacto"],
            ["5 - Borrar Contacto"],
            ["0 - Cerrar Agenda"]
        ]
        
        for i in range(0, len(menu)):
            print(menu[i][0])
        
        opcion = int(input("Introduzca una opcion: "))
        
        if (opcion == 1):
            self.agregar()
        elif (opcion == 2):
            self.lista()
        elif (opcion == 3):
            self.buscar()
        elif (opcion == 4):
            self.editar()
        elif (opcion == 5):
            self.borrar()
        elif (opcion == 0):
            print("Saliendo de la agenda...")
            exit()
            
    def agregar(self):
        nombre = input("Introduzca un nombre: ")
        telefono = input("Introduzca el telefono: ")
        email = input("Introduzca el email: ")
        self.contactos.append({'nombre':nombre, 'telefono':telefono, 'email':email})
        
    def lista(self):
        if len(self.contactos) == 0:
            print("No hay contactos.", end="\n\n")
        else:
            for i in range(0, len(self.contactos)):
                print(self.contactos[i]['nombre'], self.contactos[i]['telefono'], self.contactos[i]['email'])
    
    
    def __busqueda_lineal(self, buscado, clave):
        for indice in range(0, len(self.contactos)):
            if (buscado == self.contactos[indice][clave]):
                return indice
        return None
       
    def mostrar_contacto(self, posicion):
        if (posicion):
                print("Contacto #", posicion, ".")
                print(" ~ Nombre: ", self.contactos[posicion]['nombre'])
                print(" ~ Telefono: ", self.contactos[posicion]['telefono'])
                print(" ~ Email: ", self.contactos[posicion]['email'])
        else:
            print("... el contacto no existe.", end="\n\n")
        
    
    def buscar(self):
        if len(self.contactos == 0):
            print("No hay contactos")
        else:
            print("Buscar por: (1) > nombre, (2) > telefono, (3) email", end="\n\n") 
            opcion = input(" Opcion: ")
            if opcion == 1:
                buscado = input("Ingrese el nombre: ")
                encontrado = self.__busqueda_lineal(buscado, "nombre", self.contactos)
            elif opcion == 2:
                buscado = input("Ingrese el telefono: ")
                encontrado = self.__busqueda_lineal(buscado, "telefono", self.contactos)
            elif opcion == 3:
                buscado = input("Ingrese el email: ")
                encontrado = self.__busqueda_lineal(buscado, "email", self.contactos)
            else:
                print("Opcion incorrecta!", end="")    
            
            self.mostrar_contacto(encontrado)
                        
    def editar(self):
        if (len(self.contactos) == 0):
            print("No hay contactos")
        else:
            print("Ingrese el nombre del contacto que desea editar: ", end="\n\n")
            buscado = input(" ~ Nombre: ")
            encontrado = self.__busqueda_lineal(buscado, "nombre")
            if (encontrado):
                self.contactos[encontrado]['nombre'] = input('Nuevo @Nombre: ')
                self.contactos[encontrado]['telefono'] = input('Nuevo @Tefono: ')
                self.contactos[encontrado]['email'] = input('Nuevo @Email: ')
            else:
                print("El contacto no existe!", end="\n\n")
    
    def borrar(self):
        if (len(self.contactos) == 0):
            print("No hay contactos", end="\n\n")
        else:
            print("Ingrese el nombre del contacto que deseas eliminar: ")
            buscado = input(" ~ Nombre: ")
            encontrado = self.__busqueda_lineal(buscado, 'nombre')
            if (encontrado):
                self.contactos.pop(encontrado)
                print("Contacto eliminado!")
            else:
                print("El contacto no existe!")

if __name__=='__main__':
    agenda = Agenda()
    while (True):
        agenda.menu()
        print("Presiona un tecla...")
        input()
        os.system('cls')
    