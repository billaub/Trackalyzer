#! /usr/bin/env python
# coding=utf-8

import os
import eyed3
import mutagen


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

    def rename(self):
        pass


'''
print bcolors.OKGREEN + "Treating " + os.getcwd() + bcolors.ENDC
for file in os.listdir(os.getcwd()):
    try:
        audiofile = mutagen.File(file)
        artist = unicode(audiofile.tags.get('TPE1').text[0])
        title = unicode(audiofile.tags.get('TIT2').text[0])
        remix = " (" + unicode(audiofile.tags.get('TPE4').text[0]) + " Remix)" if audiofile.tags.get('TPE4') else ""
        new_name = artist + " - " + title + remix + ".mp3"
        new_name = new_name.replace("/", " ft. ")
        if new_name != file.decode('utf-8'):
            print "renaming\n" + file.decode('utf-8') + " --> " + new_name
        os.rename(file, new_name)
    except UnicodeDecodeError as e:
        print bcolors.FAIL + "Unicode Error with " + file + " " + str(e) + bcolors.ENDC
    except AttributeError as e:
        print bcolors.FAIL + "Attribute Error with " + file + " " + str(e) + bcolors.ENDC
        pass
    except OSError as e:
        print bcolors.FAIL + "OS Error with " + file + " " + str(e) + bcolors.ENDC
print bcolors.OKGREEN + "done" + bcolors.ENDC
'''
