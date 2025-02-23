import requests
import json
import pytest


@pytest.mark.integration
def test_integration_get_data() -> None:
    base_url = "https://api.gemini.com/v1"
    response = requests.get(base_url + "/trades/btcusd")
    btcusd_trades = response.json()
    assert isinstance(btcusd_trades, list)
    obj = btcusd_trades[0]
    assert "timestamp" in obj
    assert "timestampms" in obj
    assert "tid" in obj
    assert "price" in obj
    assert "amount" in obj
    assert "exchange" in obj
    assert "type" in obj
    assert isinstance(obj, dict)
