#!usr/bin/env python

import soundcloud

#encapsulation of strings for privacy & securityreasons
__id = "c5806c6c3a854752e9950dd16123bcb7"
__secret = "0e10af495c8b2000f8c3c29ec51abb7a"
__username = "flan12365@gmail.com"
__password = "1234567u"
# create client object with app and user credentials

client = soundcloud.Client(client_id= __id,
                           client_secret= __secret,
                           username= __username,
                           password= __password)

#sets to username
sc_username = client.get('/me').username

# retrieve sets associated with soundcloud account
playlist = client.get('/playlists/58581035')
playlist2 = client.get('/playlists/58580922')

# print each track from the playlists
for track in playlist.tracks:
    print track['title']

for track in playlist2.tracks:
	print track['title']

print sc_username