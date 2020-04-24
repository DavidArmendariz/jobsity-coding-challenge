import pika
from fetch_stock import fetch_stock

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_stock_queue')


def on_request(ch, method, props, body):
    response = fetch_stock(body)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_stock_queue', on_message_callback=on_request)

print("[x] Awaiting RPC stock requests")
channel.start_consuming()
