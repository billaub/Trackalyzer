#! /usr/bin/env python
from tagger import Tagger
from renamer import Renamer
from optparse import OptionParser
import config
import os

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-r", "--rename", action="store_false", dest="tag", default=True, help="Runs only the renamer")
    parser.add_option("-t", "--tag", action="store_false", dest="rename", default=True, help="Runs only the tagger")
    parser.add_option("-d", "--directory", action="store", dest="dir", help="Specify the directory")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="add verbose mode")
    (options, args) = parser.parse_args()
    config.RENAME = options.rename
    config.TAG = options.tag
    config.VERBOSE = options.verbose
    t = Tagger()
    r = Renamer()
    t.tag(options.dir or config.DIR or os.getcwd())
