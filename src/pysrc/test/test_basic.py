import pytest
from pysrc.data_client import DataClient

#@pytest.fixture(scope="function")
def test_get_data(mocker):
    mock_data = {
        #"prices":["93030.33", "95993.4", "93030.33"], 
        #"amounts":["0.00001", "0.00049765", "0.0001"],
        #"exchanges":["gemini", "gemini", "gemini"],
        #"types":["sell", "buy", "sell"],
        "buys": [(95993.4,0.00049765)],
        "sells": [(93030.33,0.00001),(93030.33,0.0001)],
        "midprice": 94511.865
    }
    
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data
    
    mocker.patch("requests.get",return_value=mock_response)

    obj = DataClient()
    user_data = obj.get_data(sandbox=True)
    assert user_data == mock_data


def test_basic() -> None:
    assert True


if __name__ == "__data_client__":
    pytest.main()