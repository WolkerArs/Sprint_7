class Url:

    main_url = 'https://qa-scooter.praktikum-services.ru'
    courier_url = f'{main_url}/api/v1/courier'
    login_courier_url = f'{courier_url}/login'
    orders_url = f'{main_url}/api/v1/orders'
    cancel_orders_url = f'{main_url}/api/v1/orders/cancel'

class TextResponse:

    successful_create_courier = '{"ok":true}'
    not_enough_data_create_courier = '{"message": "Недостаточно данных для создания учетной записи"}'
    duplicate_login_create_courier = '{"message": "Этот логин уже используется"}'

    not_enough_data_login_courier = '{"message":  "Недостаточно данных для входа"}'
    not_existing_courier_login_courier = '{"message": "Учетная запись не найдена"}'

class OrderData:

    order_data = [
                   {
                      "firstName": "Naruto",
                      "lastName": "Uchiha",
                      "address": "Konoha, 142 apt.",
                      "metroStation": 4,
                      "phone": "+7 800 355 35 35",
                      "rentTime": 5,
                      "deliveryDate": "2020-06-06",
                      "comment": "Saske, come back to Konoha",
                      "color": ["BLACK"]
                   },
                   {
                       "firstName": "Naruto",
                       "lastName": "Uchiha",
                       "address": "Konoha, 142 apt.",
                       "metroStation": 4,
                       "phone": "+7 800 355 35 35",
                       "rentTime": 5,
                       "deliveryDate": "2020-06-06",
                       "comment": "Saske, come back to Konoha",
                       "color": ["GREY"]
                  },
                  {
                      "firstName": "Naruto",
                      "lastName": "Uchiha",
                      "address": "Konoha, 142 apt.",
                      "metroStation": 4,
                      "phone": "+7 800 355 35 35",
                      "rentTime": 5,
                      "deliveryDate": "2020-06-06",
                      "comment": "Saske, come back to Konoha",
                      "color": []
                  },
                  {
                      "firstName": "Naruto",
                      "lastName": "Uchiha",
                      "address": "Konoha, 142 apt.",
                      "metroStation": 4,
                      "phone": "+7 800 355 35 35",
                      "rentTime": 5,
                      "deliveryDate": "2020-06-06",
                      "comment": "Saske, come back to Konoha",
                      "color": ["BLACK", "GREY"]
                  }
                ]


