import pika
from fetch_stock import fetch_stock
import time


def on_request(ch, method, props, body):
    response = fetch_stock(body.decode('utf-8'))
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


class StockServer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_stock_queue')

    def consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue='rpc_stock_queue', on_message_callback=on_request)
        self.channel.start_consuming()


if __name__ == '__main__':
    print('[x] Awaiting RPC stock requests')
    stock_server = StockServer()
    stock_server.consume()
