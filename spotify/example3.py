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
    album_id = None
    for album in albums["items"]:
        if album["name"] == nombre_album:
            album_id = album["id"]
            break

    if album_id:
        # Obtener la lista de temas del álbum
        tracks = sp.album_tracks(album_id)
        print(f"Lista de temas del álbum '{nombre_album}':")
        for track in tracks["items"]:
            print(track["name"])
    else:
        print(f"No se encontró el álbum '{nombre_album}' del artista '{nombre_artista}'.")
else:
    print(f"No se encontró el artista '{nombre_artista}'.")