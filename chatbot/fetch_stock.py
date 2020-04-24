import csv
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_stock(stock_code):
    try:
        # By default, RabbitMQ sends messages as bytestring, so we have to convert the code to a regular string.
        stock_decoded = stock_code.lower().decode('utf-8')
        payload = {'s': stock_decoded,
                   'f': 'sd2t2ohlcv', 'h': None, 'e': 'csv'}
        response = requests.get(os.environ.get('STOOQ_URL'), params=payload)
        close_price = list(csv.reader(response.text.strip().split('\n')))[0][6]
        return close_price
    except:
        return 'error'
