


import alpaca_trade_api as tradeapi

api = tradeapi.REST('PKVBXZRT0VWL3U5RQG3Y', 'Mnm9xzhzrFh2K7b3FoD2z6gIxLtth0u64XlPrNl9', base_url='https://paper-api.alpaca.markets')


api.list_positions()





barset = api.get_barset('AAPL', 'day', limit=5)
print(barset)





aapl_bars=barset['AAPL']
print(aapl_bars)



week_open = aapl_bars[0].o
week_close = aapl_bars[-1].c
percent_change = (week_close - week_open) / week_open * 100
print('AAPL moved {}% over the last 5 days'.format(percent_change))



api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)




api.list_positions()






