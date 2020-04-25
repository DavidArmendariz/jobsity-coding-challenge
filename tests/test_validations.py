from chatbot.validations import command_is_valid
import pytest

commands = [('/stock=aapl.us', True), ('/stok=aapl.us', False),
            ('/stock==aapl.us', False), ('/STOCK=AAPL.US', False),
            ('/STOCK=aapl.us', False), ('/Stock=aapl.us', False),
            ('stock=aapl.us=', False), ('/stock=aapl=us', False),
            ('/stock=AAPL.US', True), ('/stock=AAPL.us', True)]


@pytest.mark.parametrize('command,expected', commands)
def test_is_command_valid(command, expected):
    """
    Test idea: check if the command_is_valid works for differente cases.
    The cases are specified in the list "commands"
    """
    assert command_is_valid(command) == expected
