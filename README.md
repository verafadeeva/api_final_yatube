
# Yatube API

### Описание
Учебный проект по созданию REST API с использованием фреймворка Django REST Framework.

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt

```
pip install -r requirements.txt
``` 
- Выполните миграции
```
python3 manage.py migrate
```
- Запустите проект
```
python3 manage.py runserver
```


### API

#### Доступные эндпоинты

- /api/v1/posts/
- /api/v1/posts/{post_id}/comments/
- /api/v1/groups/
- /api/v1/follow/
- /api/v1/jwt/create/

#### Документация

http://127.0.0.1:8000/redoc/


#### Получить список постов:

```http
  GET /api/v1/posts/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `limit`   | `int`    | Количество публикаций на страницу|
| `offset`  | `int`    | Номер страницы после которой начинать выдачу|

#### Создание публикации

```http
  POST /api/v1/posts/
```

| Request body schema  | Type     | Description                       |
| :--------            | :------- | :-------------------------------- |
| `text`               | `string` | *Required*. Текст публикациии   |
| `image`              | `string or null <binary>` | Картинка         |
| `group`              | `int or null`             | id сообщества    |

#### Подписки

```http
  GET /api/v1/follow/
```
Анонимные запросы запрещены

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| search`   | `string` | Писк по подпискам          |