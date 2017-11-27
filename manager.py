#! /usr/bin/python
import spotipy
import spotipy.util as util
import os
from renamer import bcolors


class SpotifyManager:
    sp = None
    token_path = os.getcwd() + "/.token"
    cache_path = os.getcwd() + "/.cache-" + os.environ.get('SPOTIFY_MAIL')
    token = ""

    def __init__(self):
        self.auth()

    def get_token(self):
        if os.path.exists(self.token_path):
            with open(self.token_path) as f:
                self.token = f.read().strip("\n")
            f.close()
        else:
            self.token = util.prompt_for_user_token(os.environ.get('SPOTIFY_MAIL'))
            with open(self.token_path, "w") as f:
                f.write(self.token)
            f.close()
        self.remove_cached_token()
        return self.token

    def remove_cached_token(self):
        os.remove(self.cache_path) \
            if os.path.exists(self.cache_path) \
            else ""

    def auth(self):
        token = self.get_token()
        self.sp = spotipy.Spotify(auth=token)

    def is_authenticated(self):
        try:
            self.sp.me()
        except spotipy.client.SpotifyException as e:
            print str(e)
            print "removing " + self.token_path
            os.remove(self.token_path)
            return False
        print bcolors.OKGREEN + "Spotify Manager successfully authenticated" + bcolors.ENDC
        return True
