import requests

def obtener_eps_de_artista(artist_id, api_key):
    base_url = "https://api.discogs.com"
    headers = {
        "User-Agent": "MiAplicacion/1.0",
        "Authorization": f"Discogs token={api_key}"
    }

    # Obtener detalles de los lanzamientos del artista
    response = requests.get(f"{base_url}/artists/{artist_id}/releases", headers=headers)
    data = response.json()

    # Filtrar los lanzamientos para obtener solo los EPs
    eps = [release["title"] for release in data.get("releases", []) if "Album" in release.get("format", [])]
    return eps

# ID del artista en Discogs y tu clave de API
artist_id = 133707
api_key = "ZOdiafVaLOXhvDZTBEgSAtuIVQYfySSUTMhVXNda"

# Obtener y mostrar los EPs del artista
ep_list = obtener_eps_de_artista(artist_id, api_key)
for ep in ep_list:
    print(ep)
