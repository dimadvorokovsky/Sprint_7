# Sprint_7

Автотесты API учебного сервиса «Яндекс Самокат».

## Проверенные ручки

- создание курьера;
- авторизация курьера;
- создание заказа;
- получение списка заказов.

## Технологии

- Python;
- pytest;
- requests;
- Allure.

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest tests -v
```

## Формирование Allure-результатов

```bash
pytest tests --alluredir=allure_results
```

## Генерация Allure-отчёта

```bash
allure generate allure_results -o allure_report --clean
```