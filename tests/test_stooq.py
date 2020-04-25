import pytest
from chatbot.fetch_stock import fetch_stock

valid_stock_codes = ['aapl.us', 'goog.us', 'GOOG.US', 'AAPL.US']
invalid_existent_codes = ['aapl', 'goog', 'LFV', 'NVC']


@pytest.mark.parametrize('stock', valid_stock_codes)
def test_successful_fetch_stock(stock):
    """
    Test idea: check if for valid bytestring stock codes, data is returned
    """
    response = fetch_stock(stock)
    assert (response != 'error' and response != 'N/D') == True


@pytest.mark.parametrize('stock', invalid_existent_codes)
def test_invalid_stock_codes(stock):
    """
    Test idea: check if for invalid bytestring stock codes, the result is "N/D"
    """
    assert fetch_stock(stock) == 'N/D'
