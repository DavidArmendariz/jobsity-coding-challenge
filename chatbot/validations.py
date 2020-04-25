# Recommendation: Ideally, we should also validate that the stock code is valid here
# but we do not have a hardcoded list of symbols that can be fetched in Stooq
import pika
from pika.exceptions import ChannelClosedByBroker


def command_is_valid(command):
    try:
        splitted_command = command.split('=')
        if splitted_command[0] != '/stock':
            return False
        elif len(splitted_command) != 2:
            return False
        return True
    except:
        return False


def stock_response(stock_code, data):
    if data == 'N/D':
        return 'No information available for this stock code. Check that it is spelled correctly.'
    elif data == 'error':
        return 'Something wrong happened. Try again later.'
    else:
        return f'{stock_code} quote is ${data} per share.'


class NoActiveConsumers(Exception):
    pass


# This validations helps to see if there is any consumer of the rpc_stock_queue
def active_consumers():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    try:
        queue_state = channel.queue_declare(
            queue='rpc_stock_queue', passive=True, durable=True)
        if not queue_state.method.consumer_count:
            print(queue_state.method.consumer_count)
            raise NoActiveConsumers
        return True
    except (ChannelClosedByBroker, NoActiveConsumers):
        return False
