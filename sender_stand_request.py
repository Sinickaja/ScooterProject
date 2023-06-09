import configuration
import requests
import data


# функция для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body)  # тело post-запроса


response_order = post_new_order(data.order_body)  # возвращает тело созданного заказа
track = response_order.json()["track"]  # запоминает номер трека заказа



