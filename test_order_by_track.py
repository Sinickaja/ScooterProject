import configuration
import data
import requests
import sender_stand_request


# Тест. Проверить получение заказа по треку и что его код ответа равен 200
def test_get_order():
        return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER +"?t=" +str(sender_stand_request.track)) #str() переводит формат параметра из целочисленного в строку


response = test_get_order()
assert response.status_code == 200

