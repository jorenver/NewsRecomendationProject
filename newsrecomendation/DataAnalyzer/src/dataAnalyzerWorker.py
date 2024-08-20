import pika
import time

from dataAnalyzerService import DataAnalyzerService
from newsrecomendation.DbModel import Connect
from newsrecomendation.DbModel import Article as ar


class DataAnalyzerWorker:
    def __init__(self, host):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        channel = connection.channel()

        channel.queue_declare(queue='analyzer_queue', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='analyzer_queue', on_message_callback=do_work)

        channel.start_consuming()


def do_work(ch, method, properties, body):
    print(f'[x] Received {body.decode()}')
    time.sleep(body.count(b'.'))

    Connect.connect_to_db()
    print('Getting pending articles....')
    services = DataAnalyzerService()
    articles = ar.Article.objects(category=None)

    for doc in articles:
        category = services.get_article_category(doc)
        print(f'Category = {category}')
        if category != '':
            doc.category = category
            doc.save()
        print(doc)

    print('[x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


