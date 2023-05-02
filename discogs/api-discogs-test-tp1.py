import discogs_client

d = discogs_client.Client('example')

results = d.search('The offspring', type='artist')[1]

print(results)