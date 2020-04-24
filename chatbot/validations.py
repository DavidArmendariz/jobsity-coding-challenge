# Recommendation: Ideally, we should also validate that the stock code is valid here
# but we do not have a hardcoded list of symbols that can be fetched in Stooq


def command_is_valid(command):
    try:
        splitted_command = command.split("=")
        if splitted_command[0].lower() != "/stock":
            return False
        elif len(splitted_command) != 2:
            return False
        return True
    except:
        return False


def fetch_stock_response(stock_code, data):
    if data == "N/D":
        return "No information available for this stock code. Check that it is spelled correctly."
    else:
        return f"{stock_code} quote is ${data} per share."
