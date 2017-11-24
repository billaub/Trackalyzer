import os

config = {
    "database" : {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": os.environ.get('DB_PASSWORD'),
        "db": "fingerprint",
    },
}