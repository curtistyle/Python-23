import discogs_client
d = discogs_client.Client('band_list/1.0', user_token="ZOdiafVaLOXhvDZTBEgSAtuIVQYfySSUTMhVXNda")

results = d.search('Original Prankster', type='release')

#print(results.pages)

#artist = results[0].artists[0]

#print(artist.name)

for artist in results:
    print(artist.artists[0].name)