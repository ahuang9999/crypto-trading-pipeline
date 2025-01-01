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

    def _parse_message(self, message):
        if isinstance(message,dict):
            self.timestamps = message["timestamps"]
            self.timestampsms = message["timestampsms"]
            self.tids = message["tids"]
            self.prices = message["prices"]
            self.amounts = message["amounts"]
            self.exchanges = message["exchanges"]
            self.types = message["types"]
        else:
            for x in message:
                if isinstance(x,str): break
                self.timestamps.append(x['timestamp'])
                self.timestampsms.append(x['timestampms'])
                self.tids.append(x['tid'])
                self.prices.append(x['price'])
                self.amounts.append(x['amount'])
                self.exchanges.append(x['exchange'])
                self.types.append(x['type'])
        

    def get_data(self, sandbox):
        self._query_api(sandbox)
        return {"timestamps":self.timestamps, "timestampsms":self.timestampsms, "tids":self.tids, "prices":self.prices, 
               "amounts":self.amounts, "exchanges":self.exchanges, "types":self.types}

