import requests, json
import pytest
from pytest.mock import Mock

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

        if sandbox==false:
            base_url = "https://api.gemini.com/v1"
        else:
            base_url = "https://api.sandbox.gemini.com/v1"
        response = requests.get(base_url + "/trades/btcusd")
        btcusd_trades = response.json()
        self._parse_message(btcusd_trades)

    def _parse_message(self, message):
        for dict in message:
            timestamps.append(dict["timestamp"])
            timestampsms.append(dict["timestampms"])
            tids.append(dict["tid"])
            prices.append(dict["price"])
            amounts.append(dict["amount"])
            exchanges.append(dict["exchange"])
            types.append(dict["type"])

    def get_data(self, sandbox):
        self._query_api(sandbox)
        return {"timestamps":self.timestamps, "timestampsms":self.timestampsms, "tids":self.tids, "prices":self.prices, 
               "amounts":self.amounts, "exchanges":self.exchanges, "types":self.types}

class Tester:
    @patch('requests.get')
    def get_data_test(self, mock_get):
        mock_response = Mock()
        expected_dict = {"timestamps":[1735219599, 1735212204, 1735194282], "timestampsms":[1735219599991, 1735212204309, 1735194282364],
                         "tids":[2840141093170399, 2840141093170395, 2840141093170391], "prices":["93030.33", "95993.4", "93030.33"], 
               "amounts":["0.00001", "0.00049765", "0.0001"], "exchanges":["gemini", "gemini", "gemini"], "types":["sell", "buy", "sell"]}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response
        user_data = get_data(true)
        mock_get.assert_called_with("https://api.sandbox.gemini.com/v1/trades/btcusd")
        self.assertEqual(user_data, expected_dict)

pytest
       
    
