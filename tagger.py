#! /usr/bin/env python

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from pprint import pprint
from renamer import bcolors

from manager import SpotifyManager
import mutagen
import eyed3
import config
import os


class Tagger:
    def __init__(self):
        self.djv = Dejavu(config.CONFIG)
        self.sp = SpotifyManager()
        while not self.sp.is_authenticated():
            self.sp.auth()

    def tag(self, dir):
        for filename in os.listdir(dir):
            if os.path.isdir(dir + filename):
                self.tag(dir + filename + '/')
            else:
                song = self.djv.recognize(FileRecognizer, dir + filename)
                song = self.sp.sp.search(q=song['song_name'], type='track', limit=1)
                try:
                    song_artist = song['tracks']['items'][0]['artists'][0]['name']
                    song_name = song['tracks']['items'][0]['name']
                    pprint(song_artist + ' - ' + song_name)
                    self.apply_tags(dir + filename, song_artist, song_name)
                except IndexError:
                    print(bcolors.FAIL + "unable to get tags for " + filename + bcolors.ENDC)
                    pass
        pass

    def apply_tags(self, song, artist, name):
        try:
            f = mutagen.File(song)
            f.tags.get('TPE1').text[0] = artist
            f.tags.get('TIT2').text[0] = name
            f.save()
        except AttributeError as e:
            print(bcolors.FAIL + e.message + bcolors.ENDC)
        import ipdb; ipdb.set_trace()