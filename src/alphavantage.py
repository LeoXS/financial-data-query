import urllib.request
import json
import collections
from datetime import datetime

MarketValue = collections.namedtuple('MarketValue', ['timestamp', 'open', 'high', 'low', 'close', 'volume'])


class MarketData(object):

    def __init__(self, symbol, marketValues):
        self.symbol = symbol
        self.data = sorted(marketValues, key=lambda x: x.timestamp)

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)


class AlphaVantage(object):

    queryTemplate = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apikey}"

    def __init__(self, clientKey):
        self.clientKey = clientKey

    def query(self, symbol):
        req = self.queryTemplate.format(symbol=symbol, apikey=self.clientKey)
        mkData = []
        with urllib.request.urlopen(req) as f:
            rawData = json.loads(f.read())
            rawData.pop("Meta Data")
            for dt, mk in next(iter(rawData.values())).items():
                newMk = MarketValue(timestamp=datetime.strptime(dt, "%Y-%m-%d"),
                                    open=float(mk["1. open"]),
                                    high=float(mk["2. high"]),
                                    low=float(mk["3. low"]),
                                    close=float(mk["4. close"]),
                                    volume=float(mk["5. volume"]))
                mkData.append(newMk)
        return MarketData(symbol, mkData)



if __name__ == "__main__":
    dataQuerier = AlphaVantage("WGTCZMVQIT2F0E69")
    mkData = dataQuerier.query("MSFT")
    for mk in mkData:
        print(mk)
