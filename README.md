# ITiCo Test  
Веб приложение + сервис, которое дает возможность логинить и регистрировать пользователя.  
Используемые технологии:  
- Docker + Docker Compose (контейнеризация приложения)  
- Django (Веб фреймворк для приложения)  
- DRF (API запросы)  
- Bootstrap (CSS стили)  

## Начнем!  
- Клонируем репозиторий:  
```
git clone git@github.com:korsilyn/ITiCo-Task.git
```
- Запускаем и собираем контейнер, затем выходим из него:  
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
(WIP)  
