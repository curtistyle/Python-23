import requests

def obtener_id_de_artista(nombre_artista, api_key):
    base_url = "https://api.discogs.com"
    headers = {
        "User-Agent": "MiAplicacion/1.0",
        "Authorization": f"Discogs token={api_key}"
    }

    # Obtener detalles del artista
    response = requests.get(f"{base_url}/database/search", headers=headers, params={"artist": nombre_artista})
    data = response.json()

    
    # Obtener el ID del primer resultado (puedes ajustar esto según tu necesidad)
    if "results" in data and len(data["results"]) > 0:
        artist_id = data["results"]
        return artist_id

    return None


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


# Nombre del artista y tu clave de API
artist_id = obtener_id_de_artista(nombre_artista, api_key)