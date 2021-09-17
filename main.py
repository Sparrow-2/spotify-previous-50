import requests
import json
from secrets import spotify_user_id, spotify_token, auto_setttings
class Save50:
    def __init__(self):

        self.spotify_token = spotify_token
        self.spotify_user_id =spotify_user_id
        self.auto_setttings = auto_setttings
        self.tracks =""


    def Findsongs(self):
        query ="https://api.spotify.com/v1/me/player/recently-played?limit=50"
        response= requests.get(query, headers = self.auto_setttings)
        response_json = response.json()
        print(response_json)
        for i in response_json ['items']:
            self.tracks +=(i["track"]["uri"]+ ",")
        self.tracks=self.tracks[:-1]
        print(self.tracks)
        self.Add_to_Playlist()
    def CreatePlaylist(self):
        query ="https://api.spotify.com/v1/users/{}/playlists".format(self.spotify_user_id)
        requests_body = json.dumps({
            "name": " previous 50", "description" : "previous 50n songs i listened to", "public" : True
        })
        response = requests.post(query, data=requests_body, headers=self.auto_setttings)
        response_json=response.json()
        print(response_json)
        return response_json['id']
    def Add_to_Playlist(self):
        self.new_playlist_id = self.CreatePlaylist()
        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.new_playlist_id, self.tracks)
        response = requests.post(query, headers=auto_setttings)
        print(response.json())

    def Last(self):
        print("start the program")
        self.Findsongs()






a=Save50()
a.Last()


