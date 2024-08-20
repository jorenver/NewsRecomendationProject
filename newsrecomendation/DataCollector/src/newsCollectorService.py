from newsapi import NewsApiClient
from newsrecomendation.DbModel import Connect
from newsrecomendation.DbModel import Article as ar


class NewsCollectorService:
    def __init__(self):
        self.key = '0b78a1df1e264b8cb9d46128246174fc'
        self.newsapi = NewsApiClient(api_key=self.key)
        Connect.connect_to_db()

    def get_sources(self):
        sources = self.newsapi.get_sources()
        return sources['sources']

    def get_articles(self, source):
        response = self.newsapi.get_everything(sources=source,
                                               language='en',
                                               sort_by='relevancy',
                                               page=1)
        return response['articles']

    def is_valid_article(self, article):
        return article['title'] is not None and \
            article['description'] is not None and \
            article['url'] is not None and \
            article['urlToImage'] is not None and \
            article['content'] is not None

    def save_article(self, a):
        if self.is_valid_article(a):
            na = ar.Article(
                author=a['author'],
                title=a['title'],
                description=a['description'],
                url=a['url'],
                urlToImage=a['urlToImage'],
                content=a['content']
            )

            na.save()

            return na
        return None
