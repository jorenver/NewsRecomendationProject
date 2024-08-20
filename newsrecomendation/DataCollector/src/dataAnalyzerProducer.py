import pika
import sys


class DataAnalyzerProducer:
    def __init__(self, host):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='analyzer_queue', durable=True)

    def send_message(self):
        print('send_message')
        message = ' '.join(sys.argv[1:]) or "Hello World!"
        self.channel.basic_publish(
            exchange='',
            routing_key='analyzer_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            ))
        print(f" [x] Sent {message}")
        self.connection.close()
