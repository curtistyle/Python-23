from heap import HeapMax, HeapMin
from os import system
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Actividad:
    def __init__(self, prioridad, descripcion, supervisor, hora, cantidad=0) -> None:
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.supervisor = supervisor
        self.hora = hora
        self.cantidad = cantidad # cantidad de Stormtroopers
    
    def __str__(self):
        return f"{__class__.__name__}({self.prioridad}, {self.descripcion}, {self.hora})"
    
    def __repr__(self):
        if not self.cantidad > 0:
            return f"El {self.descripcion} a las {self.hora}. P:{self.prioridad}"
        else:
            return f"El {self.descripcion} a las {self.hora}. Cantidad de Stormtroopers {self.cantidad}. P:{self.prioridad}"
    
    def __lt__(self, otra_actividad):
        return self.prioridad < otra_actividad.prioridad
        

base_starkiller = HeapMax()

lista_de_operaciones = [
    Actividad(3, "Snoke's ordena: atacar a la Resistencia", "Snoke's", "08:00"),
    Actividad(1, "General's comanda: patrullar el sector 5", "General Hux", "09:45", cantidad=22),
    Actividad(1, "General Hux's comanda: gestion de recursos", "General Hux", "08:15"),
    Actividad(2, "Phasma's ordena: investigar actividad sospechosa en el sector 9", "Phasma's", "07:30", cantidad=10),
    Actividad(2, "Phasma's ordena: reforzar tropas en la torre norte ", "Phasma's", "10:00"),   
    Actividad(3, "Kylo Ren's ordena: localizar al droide", "Kylo Ren's", "09:00"),
    Actividad(1, "General's comanda: mantenimiento de sistemas defensivos", "General Hux", "11:00"),
    Actividad(2, "Kylo Ren solicita analizar información de prisioneros", "Kylo Ren", "22:00"),
    Actividad(3, "Snoke ordena el despliegue de cazas alrededor de la base", "Snoke", "23:00")
]

for operacion in lista_de_operaciones:
    base_starkiller.arrive(operacion, operacion.prioridad)

contador = 0
while (len(base_starkiller.elements) > 0):
    contador +=1
    operacion :Actividad = base_starkiller.atention()[1]

    print(f"#{contador} {color.RED}Operacion en curso: \'{repr(operacion)}\'{color.END}")
    print(".")
    print(".")
    print(".")
    
    if (contador == 5):
        nueva_actividad = Actividad(1, "Phasma ordena: revision de intrusos en el hangar B7", "Phasma", "00:00", 25)
        base_starkiller.arrive(nueva_actividad, 1)
        print(f"¡Se agrego una nueva operacion del supervisor: {color.GREEN}{nueva_actividad.supervisor}{color.END}!")
    
    if (contador == 6):
        prioridad_siquiente=base_starkiller.elements[0][0]

        nueva_actividad = Actividad(prioridad_siquiente, "Snoke ordena: destruir el planeta Takodana", "Snoke", "00:00", 25)
        
        base_starkiller.arrive(nueva_actividad, prioridad_siquiente)
        
        print(f"¡Se agrego una nueva operacion del supervisor: {color.GREEN}{nueva_actividad.supervisor}{color.END}!")
                
    
    print(f"¿Quiere agregar una nueva operacion (S/N)?")
    if str(input()).upper() == "S":
        prioridad = int(input("Ingrese la prioridad: "))
        supervisor = input("Ingrese el supervisor: ")
        descripcion = input("Ingrese una descripcion: ")
        hora = input("Ingrese la hora: ")
        cantidad = int(input("Ingrese la cantidad de Stormtroopers: "))
        nueva_actividad = Actividad(prioridad, descripcion, supervisor, hora, cantidad)
        base_starkiller.arrive(nueva_actividad, nueva_actividad.prioridad)
        print(f"\n¡Se agrego una nueva operacion del supervisor: {color.GREEN}{nueva_actividad.supervisor}{color.END}!")
        input()

    system("cls")
    