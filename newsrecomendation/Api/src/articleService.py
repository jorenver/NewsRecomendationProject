from newsrecomendation.DbModel import Article as ar, Connect


class ArticleService:
    def __init__(self):
        Connect.connect_to_db()

    def get_articles(self, category):
        articles = ar.Article.objects(category=category)
        response = []

        for a in articles:
            response.append({
                'author': a.author,
                'title': a.title,
                'description': a.description,
                'url': a.url,
                'urlToImage': a.urlToImage,
                'category': a.category
            })
        return response

    def get_categories(self):
        pipeline = [
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]

        result = ar.Article.objects.aggregate(pipeline)

        categories = []
        for item in result:
            category = item['_id']

            if category is not None:
                categories.append(item['_id'])

        return categories
