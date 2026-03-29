import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info
print(type(info))

# # print(info.keys())
# print(len(info))
# print(info['shortName'])
# print(info['longName'])
# print(info['currentPrice'])

# print(info['longbusinesssummary'])

# print(info['longbusinesssummary'].split())
# print('iPhone' in info['longBusinessSummary'].split())

# print('iPhone' in info['longBusinessSummary'])

# print(info['city'])
# info['city'][0] = 'c'
# info['city'] = 'Wellesley'
# print(info['city'])

# info['founder'] = 'Robert'
# print(info['founder'])

# for k,v in info.items():
#     print(k,v)

# tickers = ['AAPL', 'GOOG', 'MSFT']
# prices = {}
# for t in tickers:
#     prices[t] = yf.Ticker(t).info['currentPrice']

# print(prices)

# print(sorted(prices)) # create a new list of the keys, sorted alphabetically
# print(sorted(prices.keys())) # same as above
# print(sorted(prices.values(), reverse=True)) # create a new list of the values, sorted from high to low

# how to sort stocks by values, but still to show k:v?

# print(info['shortName'])
# print(info['currentPrice'])

tickers.append('GOOG')
print(tickers)
# tickers = {}
for t in tickers: 
    tickers[t] = yf.Ticker(t).info['currentPrice']
print(prices)


