import os
CONFIG = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": os.getenv("DB_PASSWORD"),
        "db": "fingerprint"
    }
}

DIR = os.getenv('MUSIC_DIR')
RENAME = True
TAG = True
VERBOSE = False