#! /usr/bin/env python
# coding=utf-8

import os
import mutagen
import config


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Renamer:
    def __init__(self):
        pass

    def rename(self, song, dir):
        try:
            if config.VERBOSE:
                print("Try renaming: " + song)
            audiofile = mutagen.File(song)
            artist = unicode(audiofile.tags.get('TPE1').text[0])
            title = unicode(audiofile.tags.get('TIT2').text[0])
            remix = " (" + unicode(audiofile.tags.get('TPE4').text[0]) + " Remix)" if audiofile.tags.get('TPE4') else ""
            new_name = artist + " - " + title + remix + ".mp3"
            new_name = dir.decode('utf-8') + new_name.replace("/", " ft. ")
            if new_name != song.decode('utf-8'):
                print "renaming\n" + song.decode('utf-8') + " --> " + new_name
            os.rename(song, new_name)
        except UnicodeDecodeError as e:
            print bcolors.FAIL + "Unicode Error with " + song + " " + str(e) + bcolors.ENDC
        except AttributeError:
            print bcolors.FAIL + "Attribute Error with " + song + " " + " Please open this song in windows first" + bcolors.ENDC
        except OSError as e:
            print bcolors.FAIL + "OS Error with " + song + " " + str(e) + bcolors.ENDC
