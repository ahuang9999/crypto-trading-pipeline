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

    def _query_api(self, sandbox) -> None:

        if sandbox==False:
            base_url = "https://api.gemini.com/v1"
        else:
            base_url = "https://api.sandbox.gemini.com/v1"
        response = requests.get(base_url + "/trades/btcusd")
        btcusd_trades = response.json()
        self._parse_message(btcusd_trades)

    def _parse_message(self, message) -> None:
        for dict in message:
            self.timestamps.append(dict["timestamp"])
            self.timestampsms.append(dict["timestampms"])
            self.tids.append(dict["tid"])
            self.prices.append(dict["price"])
            self.amounts.append(dict["amount"])
            self.exchanges.append(dict["exchange"])
            self.types.append(dict["type"])

    def get_data(self, sandbox):
        self._query_api(sandbox)
        return {"timestamps":self.timestamps, "timestampsms":self.timestampsms, "tids":self.tids, "prices":self.prices, 
               "amounts":self.amounts, "exchanges":self.exchanges, "types":self.types}
