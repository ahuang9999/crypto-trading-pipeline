import pytest
from pytest_mock import MockerFixture
from pysrc.data_client import DataClient


def test_get_data(mocker: MockerFixture) -> None:
    mock_api_response = [
        {"price": "95993.4", "amount": "0.00049765", "type": "buy"},
        {"price": "93030.33", "amount": "0.00001", "type": "sell"},
        {"price": "93030.33", "amount": "0.0001", "type": "sell"},
    ]
    mock_data = {
        "buys": [(95993.4, 0.00049765)],
        "sells": [(93030.33, 0.00001), (93030.33, 0.0001)],
        "midprice": 94511.86,
    }

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_api_response
    mocker.patch("requests.get", return_value=mock_response)

    obj = DataClient()
    user_data = obj.get_data(sandbox=True)
    assert user_data == mock_data


def test_basic() -> None:
    assert True


if __name__ == "__data_client__":
    pytest.main()
