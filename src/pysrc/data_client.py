import requests #type: ignore
import json
import time


class DataClient:
    def __init__(self) -> None:
        self.buys: list[tuple[float, float]] = []
        self.sells: list[tuple[float, float]] = []
        self.midprice: float

    def _query_api(self, sandbox: bool) -> None:
        if sandbox:
            base_url = (
                "https://api.gemini.com/v1/trades/btcusd?since_tid=0&limit_trades=3"
            )
            response = requests.get(base_url)
        else:
            base_url = "https://api.sandbox.gemini.com/v1"
            current_time = time.time()
            response = requests.get(
                base_url + "/trades/btcusd" + "?timestamp=" + str(current_time)
            )

        btcusd_trades = response.json()

        self._parse_message(btcusd_trades)

    def _parse_message(self, message: list[dict]) -> None:
        lowestAsk: float = 1000000.0
        highestBid: float = 0.0
        for x in message:
            if isinstance(x, str):
                break
            elPrice: float = float(x["price"])
            if x["type"] == "buy":
                if elPrice < lowestAsk:
                    lowestAsk = elPrice
                self.buys.append((elPrice, float(x["amount"])))
            else:
                if elPrice > highestBid:
                    highestBid = elPrice
                self.sells.append((elPrice, float(x["amount"])))
        self.midprice = round((lowestAsk + highestBid) / 2, 3)

    def get_data(self, sandbox: bool) -> dict:
        self._query_api(sandbox)
        return {"buys": self.buys, "sells": self.sells, "midprice": self.midprice}
