import requests

def obtener_albumes_de_artista(artist_id, api_key):
    base_url = "https://api.discogs.com"
    headers = {
        "User-Agent": "MiAplicacion/1.0",
        "Authorization": f"Discogs token={api_key}"
    }

    # Obtener la lista de álbumes de un artista
    response = requests.get(f"{base_url}/artists/{artist_id}/releases", headers=headers)
    data = response.json()

    return data

# ID del artista en Discogs y tu clave de API
artist_id = "133707"
api_key = "ZOdiafVaLOXhvDZTBEgSAtuIVQYfySSUTMhVXNda"

# Obtener y mostrar los álbumes del artista
albumes = obtener_albumes_de_artista(artist_id, api_key)
for album in albumes["releases"]:
    print(album["title"])
    