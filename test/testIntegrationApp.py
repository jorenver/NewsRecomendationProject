import unittest
from newsrecomendation.Api.src.app import app
from unittest.mock import patch


class FlaskIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('newsrecomendation.Api.src.articleService.ArticleService.get_articles')
    def test_get_articles(self, mock_get_articles):
        mock_get_articles.return_value = [
            {'author': 'Author 1', 'title': 'Title 1', 'description': 'Desc 1', 'url': 'http://example.com/1', 'urlToImage': 'http://example.com/img1', 'category': 'tech'},
            {'author': 'Author 2', 'title': 'Title 2', 'description': 'Desc 2', 'url': 'http://example.com/2', 'urlToImage': 'http://example.com/img2', 'category': 'tech'}
        ]

        response = self.app.get('/articles?category=tech')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]['author'], 'Author 1')
        self.assertEqual(response.json[0]['category'], 'tech')
        self.assertEqual(response.json[0]['category'], 'tech')

    @patch('newsrecomendation.Api.src.articleService.ArticleService.get_categories')
    def test_get_categories(self, mock_get_categories):
        mock_get_categories.return_value = ['tech', 'health']

        response = self.app.get('/categories')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ['tech', 'health'])


if __name__ == '__main__':
    unittest.main()