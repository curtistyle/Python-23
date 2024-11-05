from grafo import Graph
from bs4 import BeautifulSoup
from random import randint

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


class Puerto:
    def __init__(self, nombre, ubicacion, provincia) -> None:
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.provincia = provincia
    
    def __repr__(self) -> str:
        return f"Puerto \'{self.nombre}\' de la ciudad \'{self.ubicacion}\' en la provincia \'{self.provincia}\'."
    
    def __eq__(self, value) -> bool:
        return self.nombre == value.nombre
    
    def __ne__(self, value) -> bool:
        return self.nombre != value.nombre
    
    def __lt__(self, value) -> bool:
        return self.nombre < value.nombre
    
    def __le__(self, value) -> bool:
        return self.nombre <= value.nombre
    
    def __gt__(self, value) -> bool:
        return self.nombre > value.nombre
    
    def __ge__(self, value) -> bool:
        return self.nombre >= value.nombre

grafo = Graph(dirigido=False)

with open('temp.html', 'r', encoding="UTF-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

rows = soup.find_all('tr')[1:]

puertos = []

for row in rows:
    cells = list(row.find_all('td'))
    
    puerto = cells[0].text.strip()
    ubicacion = cells[2].text.strip()
    localidad_provincia = cells[3].text.strip()
    
    # print(f"{puerto=}, {ubicacion=}, {localidad_provincia=}")
    
    
    puertos.append(Puerto(puerto, ubicacion, localidad_provincia))

for puerto in puertos:
    grafo.insert_vertice(puerto)

temp_puertos = puertos.copy()

for puerto_a in puertos:
    for puerto_b in temp_puertos:

            if (puerto_a == puerto_b):
                encontrado=grafo.exist_path(puerto_a, puerto_b)
                if (encontrado == True):
                    print(f"{puerto_a=}, {puerto_b=}")
                if (encontrado == False):
                    grafo.insert_arista(puerto_a, puerto_b, 0)
            else:    
                grafo.insert_arista(puerto_a, puerto_b, randint(10, 10000))
        

for nodo in grafo.elements:
    print(f"El puerto {color.YELLOW}{nodo['value'].nombre}{color.END} se relaciona con")
    for adyacente in nodo['aristas']:
        print(f" -> {color.PURPLE}{adyacente['value'].nombre}{color.END} que esta a {color.BLUE}{adyacente['peso']}{color.END} Km")
    input()