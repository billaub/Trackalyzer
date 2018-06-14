#! /usr/bin/env python

import os
from pprint import pprint

import mutagen
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

import config
from manager import SpotifyManager
from renamer import Renamer
from renamer import bcolors


class Tagger:
    def __init__(self):
        if config.TAG:
            self.djv = Dejavu(config.CONFIG)
            self.sp = SpotifyManager()
            while not self.sp.is_authenticated():
                self.sp.auth()

    def tag(self, dir):
        for filename in os.listdir(dir):
            if os.path.isdir(dir + filename):
                self.tag(dir + filename + '/')
                continue
            if config.TAG:
                if config.VERBOSE:
                    print("Tagging: " + dir + filename)
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
                except:
                    print(bcolors.FAiL + "Wrong file type: " + filename + bcolors.ENDC)
                    pass
            if config.RENAME:
                r = Renamer()
                r.rename(dir + filename, dir)
        pass

    def apply_tags(self, song, artist, name):
        try:
            f = mutagen.File(song)
            f.tags.get('TPE1').text[0] = artist
            f.tags.get('TIT2').text[0] = name
            f.save()
        except AttributeError as e:
            print(bcolors.FAIL + e.message + bcolors.ENDC)
