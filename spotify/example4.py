import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credenciales de la aplicación
client_id = "TU_CLIENT_ID"
client_secret = "TU_CLIENT_SECRET"

# Inicializar el objeto de autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Nombre del artista y nombre del álbum
nombre_artista = "Nombre_del_artista"
nombre_album = "Nombre_del_album"

# Buscar el artista
results = sp.search(q=nombre_artista, type="artist", limit=1)
if "artists" in results and "items" in results["artists"]:
    artist = results["artists"]["items"][0]
    artist_id = artist["id"]

    # Buscar el álbum del artista
    albums = sp.artist_albums(artist_id, album_type="album")
    album_info = None
    for album in albums["items"]:
        if album["name"] == nombre_album:
            album_info = album
            break

    if album_info:
        # Obtener información detallada del álbum
        album_id = album_info["id"]
        album_details = sp.album(album_id)
        print("Información del álbum:")
        print("Título:", album_details["name"])
        print("Artista:", ", ".join([artist["name"] for artist in album_details["artists"]]))
        print("Fecha de lanzamiento:", album_details["release_date"])
        print("Géneros:", ", ".join(album_details["genres"]))
        print("Enlace al álbum:", album_details["external_urls"]["spotify"])
    else:
        print(f"No se encontró el álbum '{nombre_album}' del artista '{nombre_artista}'.")
else:
    print(f"No se encontró el artista '{nombre_artista}'.")