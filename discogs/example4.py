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
        artist_id = data["results"][0]["id"]
        return artist_id

    return None

# Nombre del artista y tu clave de API

nombre_artista = input("Ingrese el nombre del artista: ")
api_key = "ZOdiafVaLOXhvDZTBEgSAtuIVQYfySSUTMhVXNda"

# Obtener y mostrar el ID del artista
artist_id = obtener_id_de_artista(nombre_artista, api_key)
if artist_id:
    print(f"El ID del artista '{nombre_artista}' es: {artist_id}")
else:
    print(f"No se encontró el artista '{nombre_artista}'.")


