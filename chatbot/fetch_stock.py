import csv
import requests


def fetch_stock(stock_code):
    stock_code_lowercase = stock_code.lower().decode("utf-8")
    with requests.Session() as session:
        url = f'https://stooq.com/q/l/?s={stock_code_lowercase}&f=sd2t2ohlcv&h&e=csv'
        download = session.get(url)
        decoded_content = download.content.decode('utf-8')
        content = csv.reader(decoded_content.splitlines(), delimiter=',')
        data = list(content)[1]
    return data[6]
