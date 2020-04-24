import pytest
from chatbot.fetch_stock import fetch_stock

valid_stock_codes = [b'aapl.us', b'goog.us', b'GOOG.US', b'AAPL.US']
invalid_existent_codes = [b'aapl', b'goog', b'LFV', b'NVC']
invalid_formatted_codes = ['aapl.us', 'goog.us', 'LFV', 'NVC']


@pytest.mark.parametrize('stock', valid_stock_codes)
def test_successful_fetch_stock(stock):
    response = fetch_stock(stock)
    assert (response != 'error' and response != 'N/D') == True


@pytest.mark.parametrize('stock', invalid_existent_codes)
def test_invalid_stock_codes(stock):
    assert fetch_stock(stock) == 'N/D'


@pytest.mark.parametrize('stock', invalid_formatted_codes)
def test_invalid_formatted_stock_codes(stock):
    response = fetch_stock(stock)
    assert response == 'error'
