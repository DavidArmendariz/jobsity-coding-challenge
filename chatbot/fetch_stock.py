import csv
import requests
from validations import fetch_stock_response


def fetch_stock(stock_code):
    # By default, RabbitMQ sends messages as bytestring, so we have to convert the code to a regular string.
    stock_decoded = stock_code.lower().decode("utf-8")
    with requests.Session() as session:
        url = f'https://stooq.com/q/l/?s={stock_decoded}&f=sd2t2ohlcv&h&e=csv'
        download = session.get(url)
        decoded_content = download.content.decode('utf-8')
        content = csv.reader(decoded_content.splitlines(), delimiter=',')
        data = list(content)[1]
    return fetch_stock_response(stock_decoded, data[6])
