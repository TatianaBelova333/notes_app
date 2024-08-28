# Note Application
Данное приложение предназначено для создания, обновления и просмотра личных заметок пользователя.<br>
Для нахожедения и автоматического устранения орфографических ошибок используется сервис Яндекс Спеллер.

### Technology Stack
* Python 3.12
* FASTAPI 0.112.1
* PostgreSQL
* Docker
* asyncpg

### Installation
Запус приложения локально осуществляется через Docker.

1. Клонировать репозиторий
```
git clone git@github.com:TatianaBelova333/notes_app.git
```
2. В корне проекта создать файл .env по типу env.example
3. Находясь в корне проекта запустить команду
```
docker compose up -d
```
### API request examples
Swagger документация - http://127.0.0.1:8000/docs

1. Регистрация пользователя
```
POST /auth/register
Content-Type: application/json
{
  "email": "example@mail.ru",
  "pasword": "12345678",
}
```

```
Content-Type: application/json
HTTP/1.1 201 Created

{
  "id": 1,
  "email": "example@mail.ru",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```

2. Авторизация
```
POST /auth/jwt/login
Content-Type: application/x-www-form-urlencoded
username=example@mail.ru&password=12345678

```
```
Content-Type: application/json
HTTP/1.1 200 OK
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE3MjQ4NTE4NTJ9.JLGtfM3FwyY5MIXRlXcoA-5zU_cwtF0c9mwx4R5qmJY",
    "token_type": "bearer"
}
```
3. Создание новой заметки авторизованным пользователем.
Content - обязательное поле. Tag и priority - опциональны.
```
POST /notes
Content-Type: application/json
{
  "content": "Купитьь малоко и мосло"
}
```

```
Content-Type: application/json
HTTP/1.1 201 Created

{
    "content": "Купить молоко и масло",
    "priority": "Неважное",
    "tag": "Разное",
    "id": 1,
    "created_at": "2024-08-28T12:54:15.953311",
    "updated_at": null,
    "user_id": 1,
    "title": "Купить молоко и масло"
}
```
4. Получение всех заметок авторизованного пользователя.
Доступна фильтрация заметок по created_at, а также поиск по полю content.
```
GET /notes?content__ilike=машину
```

```
Content-Type: application/json
HTTP/1.1 201 Created

[
    {
        "content": "Купить машину",
        "priority": "Неважное",
        "tag": "Разное",
        "id": 2,
        "created_at": "2024-08-28T14:01:17.743063",
        "updated_at": null,
        "user_id": 1,
        "title": "Купить машину"
    }
]
```

### Authors
[Tatiana Belova](https://github.com/TatianaBelova333)
