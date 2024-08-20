import mongoengine as me


def connect_to_db():
    me.connect(
        db='newsbase',
        host='localhost',
        port=27017
    )
