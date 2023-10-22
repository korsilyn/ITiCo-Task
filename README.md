# ITiCo Test  
Веб приложение (Backend + API), которое дает возможность регистрировать пользователя, получать ключ сессии при входе и выходить из аккаунта.  
Используемые технологии:  
- Docker + Docker Compose (контейнеризация приложения)  
- Django (Веб фреймворк для приложения)  
- DRF (API запросы)  
- dj-rest-auth (Auth API запросы)  
- Bootstrap (CSS стили)  
- SQLite3 (DB)  

## Начнем!  
- Клонируем репозиторий:  
```
git clone git@github.com:korsilyn/ITiCo-Task.git
```
- Запускаем и собираем контейнер, затем остановим его при помощи Ctrl + C:  
```
sudo docker compose up --build
```
- Запускаем миграции:  
```
sudo docker compose run web itico/manage.py migrate
```
- Запускаем веб-приложение:  
```
sudo docker compose up -d
```

## Примеры API запросов:  
### Auth Register  
Регистрация пользователя:  
```curl
curl --location --request POST '127.0.0.1:8000/api/registration/' \  
--header 'Content-Type: application/json' \  
--data-raw '{
    "username": "test-user",
    "password1": "qqwwee123",
    "password2": "qqwwee123"
}'
```  
### Auth Login
Вход пользователя:  
```curl
curl --location --request POST '127.0.0.1:8000/api/login/' \  
--header 'Content-Type: application/json' \  
--data-raw '{
    "username": "test-user",
    "password": "qqwwee123"
}'
```  
Пример ответа:
```json
{
    "key": "ce63bef2ea5030e163170b3b299367baf56c4ee3"
}
```  
### Auth Logout
Логаут пользователя:  
```curl
curl --location --request POST '127.0.0.1:8000/api/logout/'  
```  
Пример ответа:
```json
{
    "detail": "Successfully logged out."
}
```  
