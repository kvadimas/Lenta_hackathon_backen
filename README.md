# Команда №1. Хакатон: сервис для работы с данными предсказательной модели.

## Описание

Серверное приложение (API), которое предназначено для работы с данными предсказательной модели через интерфейс пользователя.

Принципиальная схема проекта:

![Принципиальная схема проекта](https://ltdfoto.ru/images/2023/10/10/Flowchart-Diagram.png "Принципиальная схема проекта.")

[Схема БД](https://dbdiagram.io/d/Lenta-6514af0cffbf5169f0a2a6e1)


## Сведения о команде

Проект разработан командой:

- **Вадим Куроткин**
- **Евгений Быковский**

## Ссылки на проекты коллег

[Шаблон сайта](https://www.figma.com/file/oDb87wsTRHsC8vTtINeoBL/Команда-№1-In-Flames%2C-Хакатон.-Лента?type=design&node-id=143-3273&mode=design&t=XnoAmzIit4khUqGa-0)

[Frontend](https://github.com/Jane-Doe666/lenta)

[Machine Learning](https://github.com/aminaadzhieva/lenta-hackathon-demand-forecasting/)

## Демонстрация

[Демо](http://31.129.111.234/)

[Документация](http://31.129.111.234/api/docs/)

## Инструкция по сборке и запуску

Для сборки и запуска проекта выполните следующие шаги:

1. Клонируйте репозиторий с помощью команды:

```bash
git clone https:https://github.com/kvadimas/Lenta_hackathon_backend.git
```

2. Перейдите в директорию проекта.

3. Запустите проект с использованием Docker, выполнив команду:
```bash
docker-compose up --build
```

4. После успешной сборки и запуска проекта, откройте веб-браузер и перейдите по следующему адресу:
```bash
http://localhost:8000
```

## Стек технологий

Проект разработан с использованием следующего стека технологий:

1. Django
2. Django DRF
3. Pytest
4. Swagger
5. Docker

## Использовались библиотеки

[djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)

[drf-spectacular](https://drf-spectacular.readthedocs.io)

[openpyxl](https://openpyxl.readthedocs.io)

[python-dotenv](https://pypi.org/project/python-dotenv/)

[progress](https://pypi.org/project/progress/)
