# ITiCo Test  
Веб приложение + сервис, которое дает возможность логиниться и регестрировать пользователя.  
Используемые технологии:  
- Docker + Docker Compose (контейнеризация приложения)  
- Django (Веб фреймворк для приложения)  
- Fastapi (Веб фреймворк для API запросов)  

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
