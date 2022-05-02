from datetime import datetime
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
import ui

def main():
    print(ui.hostName)
    # mt.initialize()

    # login = 0
    # password = ''
    # server = ''

    # mt.login(login, password, server)

    # account_info = mt.account_info()

    # print('login', account_info.login)
    # print('balance', account_info.balance)
    # print('equity', account_info.equity)

    # num_symbols = mt.symbols_total()

    # print('#Symbols', num_symbols)

    # symbols = mt.symbols_get()

    # eurusd = mt.symbol_info("EURUSD")._asdict()

    # # print(eurusd)

    # symbol_price = mt.symbol_info_tick("EURUSD")._asdict()

    # print(symbol_price)

    # ohlc_data = pd.DataFrame(mt.copy_rates_range("EURUSD", mt.TIMEFRAME_D1, datetime(2021, 1, 1), datetime.now()))

    # fig = px.line(ohlc_data, x = ohlc_data['time'], y = ohlc_data['close'])
    # fig.show()


if __name__ == "__main__":
    main()