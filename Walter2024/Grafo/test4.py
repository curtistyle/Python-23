import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_puertos():
    # URL del sitio
    url = "https://www.magyp.gob.ar/new/0-0/programas/dma/regimenes_especiales/puertos-con-habilitacion.php"
    
    # Hacer la solicitud HTTP al sitio
    response = requests.get(url)
    
    # Crear el objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar la tabla
    table = soup.find('table')
    
    # Crear listas para almacenar los datos
    headers = []
    rows = []
    
    # Obtener los encabezados de la tabla
    for th in table.find_all('th'):
        headers.append(th.text.strip())
    
    # Obtener las filas de la tabla
    for tr in table.find_all('tr'):
        row = [td.text.strip() for td in tr.find_all('td')]
        if row:
            rows.append(row)
    
    # Crear un DataFrame con los datos obtenidos
    df = pd.DataFrame(rows, columns=headers)
    
    return df

# Llamar a la función y mostrar los resultados
df_puertos = scrape_puertos()
print(df_puertos)
