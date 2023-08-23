import requests 
import json

api_key = "ZOdiafVaLOXhvDZTBEgSAtuIVQYfySSUTMhVXNda"

base_url = "https://api.discogs.com"
headers = {
    "User-Agent": "MiAplicacion/1.0",
    "Authorization": f"Discogs token={api_key}"
}


busqueda = input("Ingrese el nombre de una banda: ")
params = {"q" : busqueda}

# Buscar el nombre del artista en la base de datos
response = requests.get(f"{base_url}/database/search", headers=headers, params=params)
data = response.json()

# with open('tu_archivo.json', 'w') as jf: 
#     json.dump(data, jf)

artist_id = data['results'][0]['id']

response = requests.get(f"{base_url}/artists/{artist_id}/releases", headers=headers)
albumes = response.json()

pages = albumes['pagination']

for page in pages:
    for album in albumes["releases"]:
        print("title: ",album["title"])
        print("year: ",album['year'])
    

# with open('tu_archivo.json', 'w') as jf: 
#     json.dump(data, jf)
