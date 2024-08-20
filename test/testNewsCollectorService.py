import unittest
from unittest.mock import patch
from newsrecomendation.DataCollector.src.newsCollectorService import NewsCollectorService


class TestNewsCollectorService(unittest.TestCase):
    @patch('newsapi.NewsApiClient')
    def test_get_sources(self, mockNewsApiClient):
        mock_newsapi_instance = mockNewsApiClient.return_value

        mock_newsapi_instance.get_sources.return_value = {
            'sources': [
                {'id': 'bbc-news', 'name': 'BBC News'},
                {'id': 'cnn', 'name': 'CNN'}
            ]
        }

        service = NewsCollectorService()
        service.newsapi = mock_newsapi_instance

        sources = service.get_sources()

        self.assertEqual(sources, [
            {'id': 'bbc-news', 'name': 'BBC News'},
            {'id': 'cnn', 'name': 'CNN'}
        ])

        mock_newsapi_instance.get_sources.assert_called_once()

    @patch('newsapi.NewsApiClient')
    def test_get_articles(self, mockNewsApiClient):
        mock_newsapi_instance = mockNewsApiClient.return_value

        mock_newsapi_instance.get_everything.return_value = {
            'articles': [
                {
                    'title': 'abc title',
                    'description': 'description abc',
                    'url': 'www.abc.com',
                    'urlToImage': 'www.abc.com/image',
                    'content': 'abc content'
                },
                {
                    'title': 'def title',
                    'description': 'description def',
                    'url': 'www.def.com',
                    'urlToImage': 'www.def.com/image',
                    'content': 'def content'
                }
            ]
        }

        service = NewsCollectorService()
        service.newsapi = mock_newsapi_instance

        articles = service.get_articles('my source')

        self.assertEqual(articles, [
            {
                'title': 'abc title',
                'description': 'description abc',
                'url': 'www.abc.com',
                'urlToImage': 'www.abc.com/image',
                'content': 'abc content'
            },
            {
                'title': 'def title',
                'description': 'description def',
                'url': 'www.def.com',
                'urlToImage': 'www.def.com/image',
                'content': 'def content'
            }
        ])

        mock_newsapi_instance.get_everything.assert_called_once()


if __name__ == '__main__':
    unittest.main()