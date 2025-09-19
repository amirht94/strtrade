import ccxt
from ccxt.base.errors import NetworkError, RequestTimeout

class CCXTHandler:
    def __init__(self, exchange_name="binance"):
        self.exchange_name = exchange_name
        self.exchange = getattr(ccxt, exchange_name)()

    def fetch_ohlcv(self, symbol="BTC/USDT", timeframe="1h", limit=50):
        try:
            self.exchange.load_markets()
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            return ohlcv
        except (NetworkError, RequestTimeout) as e:
            print(f"Fetch error: {e}")
            return None
