import requests, json
class DataClient:
    def __init__(self):
        self.timestamps = []
        self.timestampsms = []
        self.tids = []
        self.prices = []
        self.amounts = []
        self.exchanges = []
        self.types = []

    def _query_api(self) -> None:

        base_url = "https://api.gemini.com/v1"
        response = requests.get(base_url + "/trades/btcusd")
        btcusd_trades = response.json()
        
        _parse_message(btcusd_trades)

    def _parse_message(self, message):
        timestamps.append(message["timestamp"]);
        timestampsms.append(message["timestampms"]);
        tids.append(message["tid"]);
        prices.append(message["price"]);
        amounts.append(message["amount"]);
        exchanges.append(message["exchange"]);
        types.append(message["type"]);

    def get_data(self):
        raise NotImplementedError
