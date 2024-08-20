import textrazor


class DataAnalyzerService:
    def __init__(self):
        self.key = 'b66c3961c7e68379d59f5916adbabb0a63e2b78b9ec250e48cba2542'

    def get_article_category(self, article):
        textrazor.api_key = self.key

        client = textrazor.TextRazor(extractors=["topics"])
        response = client.analyze_url(article.url)

        topics = response.topics()
        if len(topics) >= 1:
            return topics[0].label
        else:
            return ''

