import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credenciales de la aplicación
client_id = "aad4ffcc488644c8ac36c765382751be"
client_secret = "dccf369fdec34a9f8de258890cae5b30"

# Inicializar el objeto de autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Nombre del artista
nombre_artista = "The Offspring"

# Buscar el artista
results = sp.search(q=nombre_artista, type="artist", limit=1)
if "artists" in results and "items" in results["artists"]:
    artist = results["artists"]["items"][0]
    artist_id = artist["id"]
    
    # Obtener los álbumes del artista
    albums = sp.artist_albums(artist_id, album_type="album")

    print(f"Álbumes de '{nombre_artista}':")
    for album in albums["items"]:
        print(album["name"])
else:
    print(f"No se encontró el artista '{nombre_artista}'.")