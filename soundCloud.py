#!usr/bin/env python

import soundcloud

###############################
######### SoundCloud ##########
###############################

#encapsulation of strings for privacy & securityreasons
__id = "**redacted**"
__secret = "**redacted**"
__username = "**redacted**"
__password = "**redacted**"
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
def getAll():
	p1=[]
	p2=[]
	# print each track from the playlists
	for track in playlist.tracks:
	    p1.append(track['title'].encode('utf-8'))

	for track in playlist2.tracks:
		p2.append(track['title'].encode('utf-8'))
	d={"Username":sc_username,"Playlist":"<br>".join(p1+p2)}
	return d

print sc_username
print getAll()
