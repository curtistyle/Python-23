# El puerto TERMINAL 6 S.A. se relaciona con
#  -> LA PLATA CEREAL S.A. que esta a 882 Km
#  -> PUNTA ALVEAR S.A. que esta a 1417 Km
#  -> CARGILL S.A. COMERCIAL E INDUSTRIAL que esta a 8175 Km
#  -> ASOCIACION DE COOPERATIVAS ARGENTINAS A.C.A. COOP. LTDA. que esta a 7162 Km
#  -> S.A.C. DE EXPORTACION Y FINANCIERA LOUIS DREYFUS Y COMPAÑÍA LIMITADA. que esta a 8065 Km
#  -> "ACINDAR" INDUSTRIA ARGENTINA DE ACEROS S.A. que esta a 8197 Km
#  -> MINERA ALUMBRERA LIMITED SUC. BS.AS. que esta a 4820 Km
#  -> NAVIPAR S.A.C.I. MARITIMA Y DE TRANSPORTE que esta a 8520 Km
#  -> EUROAMERICA S.A. que esta a 1200 Km
#  -> ALFRED C. TOEPFER INTERNATIONAL S.A. que esta a 7592 Km
#  -> MULTIPUERTO S.A. que esta a 3974 Km
#  -> VICENTIN S.A.I.C que esta a 781 Km
#  -> NIDERA S.A. que esta a 8336 Km
#  -> Y.P.F S.A. que esta a 8057 Km
#  -> RESINFOR METANOL S.A. que esta a 5834 Km
#  -> TERMINAL ZARATE S.A. que esta a 3744 Km
#  -> T.A.G.S.A. que esta a 927 Km
#  -> MADERERA RIO PARANA, margen derecha S.A. que esta a 5234 Km
#  -> CALETA PAULA que esta a 3352 Km
#  -> SIDERAR S.A.I.C que esta a 511 Km
#  -> PUERTO DIAMANTE S.A que esta a 2961 Km
#  -> DELTA DOCK S.A. que esta a 8625 Km
#  -> ALFRED TOEPFER INTERNATIONAL ARGENTINA S.R.L.( ex TRADIGRAIN S.A.) que esta a 3842 Km
#  ->  que esta a 605 Km
#  -> PUERTO USHUAIA que esta a 6160 Km
#  -> SAN ANTONIO ESTE que esta a 3084 Km
#  -> BARRANQUERAS que esta a 7729 Km
#  -> PUERTO NUEVO DE LA CIUDAD DE FORMOSA que esta a 8704 Km
#  -> ESSO SOCIEDAD ANONIMA PETROLERA ARGENTINA que esta a 1496 Km
#  -> PUERTO MADRYN que esta a 9247 Km
#  -> ESSO SOCIEDAD ANONIMA PETROLERA ARGENTINA - CAMPANA que esta a 7083 Km
#  -> FAPLAC SOCIEDAD ANONIMA que esta a 7633 Km
#  -> CONSORCIO DE GESTIÓN DEL PUERTO DE BAHIA BLANCA que esta a 6486 Km
#  -> CENTRAL TERMICA SAN NICOLAS SOCIEDAD ANONIMA que esta a 7323 Km
#  -> MOLINOS RIO DE LA PLATA S.A. que esta a 4153 Km
#  -> CARGILL S.A.C.I. (AMPLIACION DTO. 122/97) que esta a 1883 Km
#  -> BUNGE ARGENTINA S.A. que esta a 5375 Km
#  -> S.A.C. DE EXPORTACION Y FINANCIERA LOUIS DREYFUS Y COMPAÑÍA LIMITADA (AMPLIACION DTO. 687/97) que esta a 3565 Km
#  -> MOLCA S.A. que esta a 9565 Km
#  -> PUERTO COMODORO RIVADAVIA que esta a 2036 Km
#  -> NOBLE ARGENTINA S.A. que esta a 5894 Km
#  -> DREYFUS TIMBÚES que esta a 4914 Km
#  -> DREYFUS TIMBÚES (Muelle de Barcazas) que esta a 3154 Km

from grafo import Graph
from random import randint

# ? grafo no dirigido
g = Graph(dirigido=False)

lista = ["A", "B", "C"]


for letra in lista:
    g.insert_vertice(letra)

temp_lista = ["A", "B", "C"]


ultima_pos = None

# print(g.elements)
# input()
# # * arista ciclo directo
# g.insert_arista("A", "A", 0)
# print(g.elements)
# input()
# g.insert_arista("A", "B", 0)
# print(g.elements)
# input()
# g.insert_arista("A", "C", 0)

# print(g.elements)


for x in lista:
    
    for y in temp_lista:
        g.insert_arista(x,y,randint(1,10))
    
    input()
    for vertice in g.elements:
        print(f"# Origen {vertice['value']} ")
        for arista in vertice['aristas']:
            print(f" --> {arista['value']}, P({arista['peso']})")


# for vertice in g.elements:
#     print(f"# Origen {vertice['value']} ")
#     for arista in vertice['aristas']:
#         print(f" --> {arista['value']}, P({arista['peso']})")
        

          
        

# for vertice in g.elements:
#     print(f"La letra {vertice['value']} se relaciona con ")
#     for adyacente in vertice['aristas']:
#         print(f" --> {adyacente['value']} : Peso({adyacente['peso']})")