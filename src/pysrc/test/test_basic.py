from unittest.mock import patch,Mock
import src.data_client

@patch('requests.get')
def test_get_data(self, mock_get):
    mock_response = Mock()
    expected_dict = {"timestamps":[1735219599, 1735212204, 1735194282], "timestampsms":[1735219599991, 1735212204309, 1735194282364],
                     "tids":[2840141093170399, 2840141093170395, 2840141093170391], "prices":["93030.33", "95993.4", "93030.33"], 
               "amounts":["0.00001", "0.00049765", "0.0001"], "exchanges":["gemini", "gemini", "gemini"], "types":["sell", "buy", "sell"]}
    mock_response.json.return_value = expected_dict
    mock_get.return_value = mock_response
    obj = data_client.DataClient()
    user_data = obj.get_data(True)
    assert user_data == expected_dict


def test_basic() -> None:
    assert True
