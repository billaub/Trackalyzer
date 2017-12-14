#! /usr/bin/env python
from tagger import Tagger
from renamer import Renamer
from optparse import OptionParser
import config

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-r", "--rename", action="store_false", dest="tag", default=True, help="Runs only the renamer")
    parser.add_option("-t", "--tag", action="store_false", dest="rename", default=True, help="Runs only the tagger")
    (options, args) = parser.parse_args()
    t = Tagger()
    r = Renamer()
    config.RENAME = options.rename
    config.TAG = options.tag
    t.tag(config.DIR)