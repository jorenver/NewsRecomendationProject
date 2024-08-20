import unittest
from unittest.mock import patch, MagicMock
from newsrecomendation.Api.src.articleService import ArticleService
from newsrecomendation.DbModel.src.Article import Article


class TestArticleService(unittest.TestCase):
    @patch('DbModel.src.Article.Article.objects')
    def test_get_articles(self, mock_objects):
        service = ArticleService()

        mock_article_1 = MagicMock(spec=Article)
        mock_article_1.author = "Author 1"
        mock_article_1.title = "Title 1"
        mock_article_1.description = "Description 1"
        mock_article_1.url = "http://example.com/1"
        mock_article_1.urlToImage = "http://example.com/img1"
        mock_article_1.category = "tech"

        mock_article_2 = MagicMock(spec=Article)
        mock_article_2.author = "Author 2"
        mock_article_2.title = "Title 2"
        mock_article_2.description = "Description 2"
        mock_article_2.url = "http://example.com/2"
        mock_article_2.urlToImage = "http://example.com/img2"
        mock_article_2.category = "tech"

        mock_objects.return_value = [mock_article_1, mock_article_2]

        result = service.get_articles(category="tech")

        expected_result = [
            {
                'author': 'Author 1',
                'title': 'Title 1',
                'description': 'Description 1',
                'url': 'http://example.com/1',
                'urlToImage': 'http://example.com/img1',
                'category': 'tech'
            },
            {
                'author': 'Author 2',
                'title': 'Title 2',
                'description': 'Description 2',
                'url': 'http://example.com/2',
                'urlToImage': 'http://example.com/img2',
                'category': 'tech'
            }
        ]
        self.assertEqual(result, expected_result)

    @patch('DbModel.src.Article.Article.objects')
    def test_get_categories(self, mock_aggregate):
        service = ArticleService()

        mock_aggregate.aggregate.return_value = [
            {"_id": "tech", "count": 50},
            {"_id": None, "count": 24},
            {"_id": "energy", "count": 12}
        ]

        result = service.get_categories()
        expected_result = ['tech', 'energy']

        self.assertEqual(result, expected_result)

        mock_aggregate.aggregate.assert_called_once_with([
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ])


if __name__ == '__main__':
    unittest.main()
