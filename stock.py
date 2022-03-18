import requests

API_KEY = 'demo'
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'+API_KEY)
if (r.status_code == 200):
    
    result = r.json()
    dataForAllDays = result['Time Series (Daily)']
    dataForSingleDate = dataForAllDays['2021-12-11']
    print dataForSingleDate['1.open']
    print dataForSingleDate['2.high']
    print dataForSingleDate['3.low']
    print dataForSingleDate['4.close']
    print dataForSingleDate['5.volume']