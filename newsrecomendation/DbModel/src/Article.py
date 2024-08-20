import mongoengine as me


class Article(me.Document):
    author = me.StringField(required=False)
    title = me.StringField(required=True)
    description = me.StringField(required=True)
    url = me.StringField(required=True)
    urlToImage = me.StringField(required=True)
    content = me.StringField(required=True)
    category = me.StringField(required=False)

    meta = {
        'collection': 'articles'
    }
