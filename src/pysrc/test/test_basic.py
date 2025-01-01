import pytest
from pysrc.data_client import DataClient

#@pytest.fixture(scope="function")
def test_get_data(mocker):
    mock_data = {
        "timestamps":[1735219599, 1735212204, 1735194282],
        "timestampsms":[1735219599991, 1735212204309, 1735194282364],
        "tids":[2840141093170399, 2840141093170395, 2840141093170391],
        "prices":["93030.33", "95993.4", "93030.33"], 
        "amounts":["0.00001", "0.00049765", "0.0001"],
        "exchanges":["gemini", "gemini", "gemini"],
        "types":["sell", "buy", "sell"]
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
