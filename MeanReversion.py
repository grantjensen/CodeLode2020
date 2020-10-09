

import alpaca_trade_api as tradeapi

api = tradeapi.REST('PKVBXZRT0VWL3U5RQG3Y', 'Mnm9xzhzrFh2K7b3FoD2z6gIxLtth0u64XlPrNl9', base_url='https://paper-api.alpaca.markets')




portfolio=api.list_positions()
for asset in portfolio:
    print(asset)




def sell():
    #Liquidates position
    portfolio=api.list_positions()
    for asset in portfolio:
        api.submit_order(
        symbol=asset.symbol,
        qty=asset.qty,
        side='sell',
        type='market',
        time_in_force='gtc'
        )




sell()
api.list_positions()



for asset in api.list_assets():
    if asset.tradable:
        print("We can trade "+str(asset.symbol))



def percent_change(asset):
    #Input: asset from api.list_assets()
    #Output: percent change from the last 5 days
    symbol=asset.symbol
    barset = api.get_barset(symbol, 'day', limit=5)
    symbol_bars=barset[symbol]
    if not symbol_bars:
        return 0
    week_open = symbol_bars[0].o
    week_close = symbol_bars[-1].c
    percent_change = (week_close - week_open) / week_open * 100
    return percent_change



print(percent_change(api.get_asset("AAPL")))




import math
def buy():
    assets_to_buy=[]
    for asset in api.list_assets()[:40]:#Only look at first 200
        if asset.tradable:
            if (percent_change(asset)<-10):
                assets_to_buy.append(asset.symbol)
    cash=float(api.get_account().cash)
    money_per_asset=cash/len(assets_to_buy)
    barset=api.get_barset(assets_to_buy,'minute',limit=1)
    for asset in assets_to_buy:
        current_price=barset[asset][0].c
        shares=money_per_asset/current_price
        #shares might not be an integer, =>
        shares=math.floor(shares)
        api.submit_order(
        symbol=asset,
        qty=shares,
        side='buy',
        type='market',
        time_in_force='gtc'
        )



buy()
print(api.list_positions())

