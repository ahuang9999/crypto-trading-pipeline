import requests, json, time

class DataClient:   
    def __init__(self):
        self.buys: list[tuple[float, float]] = []
        self.sells: list[tuple[float, float]] = []
        self.midprice: float

    def _query_api(self, sandbox) -> None:

        if sandbox==False:
            base_url = "https://api.gemini.com/v1"
        else:
            base_url = "https://api.sandbox.gemini.com/v1"
        current_time = round(time.time()*1000)

        response = requests.get(base_url + "/trades/btcusd" + "?timestampms=" + str(current_time-1000))
        btcusd_trades = response.json()
        
        self._parse_message(btcusd_trades)

    def _parse_message(self, message):
        lowestAsk: float = 1000000.0
        highestBid: float = 0.0
        for x in message:
            if isinstance(x,str): break
            if x["type"] == "buy":
                elPrice: float = float(x["price"])
                if elPrice<lowestAsk:
                    lowestAsk = elPrice
                self.buys.append((elPrice,float(x["amount"])))
            else:
                elPrice: float = float(x["price"])
                if elPrice>highestBid:
                    highestBid = elPrice
                self.sells.append((elPrice,float(x["amount"])))
        self.midprice = (lowestAsk+highestBid)/2
            
        

    def get_data(self, sandbox):
        self._query_api(sandbox)
        return {"buys": self.buys, "sells": self.sells, "midprice": self.midprice}
