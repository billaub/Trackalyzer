#! /usr/bin/python
from manager import SpotifyManager
from dejavu import Dejavu
from conf import config


djv = Dejavu(config)

sp = SpotifyManager()
if sp.is_authenticated():
    print "ok"