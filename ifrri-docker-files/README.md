# SOURCE DOCKER
 Исходники созданного образа
 
***
## Что внутри

### gytim-django-first
Простой django проект

Можно создавать и удалять записи, которые будут отображаться в таблице
Если база не заполнена предложит сделать это в самом начале

По умолчанию берет сайт рядом.

В докере можно изменить путь к коду DJANGO_PROJECT


Также для корректного развертывание данных необходимо:

##### 1) create_base.sh
  Изменить пароль, пользователя и имя базы в скрипте, либо использовать стандартные настройки.

##### 2) newsite/newsite/settings.py
  Изменить пароль, пользователя и имя базы в скрипте, либо использовать стандартные настройки.


*Можно в secret запихнуть по аналогии, но это уже в следующей версии.

***
## Commands

Для загрузки образа в hub.docker.com

```
docker build -t gytim/<name> .
docker push gytim/<name>
```

Обязательно надо войти под собой

```
docker login
```