import requests 
import json

api_key = "ZOdiafVaLOXhvDZTBEgSAtuIVQYfySSUTMhVXNda"

base_url = "https://api.discogs.com"
headers = {
    "User-Agent": "MiAplicacion/1.0",
    "Authorization": f"Discogs token={api_key}"
}

# Buscar el nombre del artista en la base de datos
response = requests.get(f"{base_url}/database/search", headers=headers, params={"q": "The Offspring"})
data = response.json()




# Obtener el ID del primer resultado que sea un artista
for result in data.get("results", []):
    if result.get("type") == "artist":
        artist_id = result.get("id")

print("ARTIST ID: ",artist_id)

response = requests.get(f"{base_url}/artists/{artist_id}/releases", headers=headers)
albumes = response.json()


# for album in albumes["releases"]:
#     print(album["title"]," - ", album["year"])


# with open('tu_archivo.json', 'w') as jf: 
#     json.dump(albumes, jf)



