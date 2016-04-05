import pika
import json

class Publisher():

    def __init__(self, config):
        self.config = config

    def publish(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.config.get('host')))
        channel = connection.channel()
        channel.exchange_declare(exchange=self.config.get('exchange'), type=self.config.get('exchange_type'))
        channel.basic_publish(exchange=self.config.get('exchange'), routing_key=message['key'], body=json.dumps(message['body']))
        connection.close()
