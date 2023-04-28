import configuration
import data
import requests


# Тест. Проверить,что код ответа равен 200
def test_get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER)


response = test_get_order()
assert response.status_code == 200
