import requests  # type: ignore
import json
import time

TIME_BETWEEN_TICKS = 6


class DataClient:
    def __init__(self) -> None:
        self.buys: list[tuple[float, float]] = []
        self.sells: list[tuple[float, float]] = []
        self.midprice: float

    def _query_api(self, sandbox: bool) -> None:
        if sandbox:
            base_url = "https://api.sandbox.gemini.com/v1/trades/btcusd?since_tid=0&limit_trades=3"
        else:
            base_url = "https://api.gemini.com/v1"
            current_time = int(time.time())
            base_url += f"/trades/btcusd?timestamp={current_time-TIME_BETWEEN_TICKS}"

        try:
            response = requests.get(base_url)
            if response.text.strip():
                btcusd_trades = response.json()
                self._parse_message(btcusd_trades)
        except json.JSONDecodeError:
            pass

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
        if lowestAsk == 1000000.0 or highestBid == 0.0:
            self.midprice = -2
        else:
            self.midprice = round((lowestAsk + highestBid) / 2, 2)

    def get_data(self, sandbox: bool) -> dict:
        self._query_api(sandbox)
        return {"buys": self.buys, "sells": self.sells, "midprice": self.midprice}
