class CourierData:
    EXISTING_LOGIN_MESSAGE = "Этот логин уже используется. Попробуйте другой."
    NOT_ENOUGH_DATA_MESSAGE = "Недостаточно данных для создания учетной записи"
    LOGIN_NOT_ENOUGH_DATA_MESSAGE = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND_MESSAGE = "Учетная запись не найдена"


class OrderData:
    BASE_ORDER = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, улица Ленина, 10",
        "metroStation": 4,
        "phone": "+7 900 123 45 67",
        "rentTime": 3,
        "deliveryDate": "2026-08-10",
        "comment": "Позвонить перед доставкой"
    }

    COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]