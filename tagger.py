#! /usr/bin/env python

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from pprint import pprint

from manager import SpotifyManager
import config
import os


class Tagger:
    def __init__(self):
        self.djv = Dejavu(config.CONFIG)
        self.sp = SpotifyManager()
        while not self.sp.is_authenticated():
            self.sp.auth()

    def tag(self, dir):
        for file in os.listdir(dir):
            if os.path.isdir(dir + file):
                self.tag(dir + file + '/')
            else:
                song = self.djv.recognize(FileRecognizer, dir + file)
                pprint(song)
        pass
