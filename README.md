# PostgreSQL + WEB(django) runing on dokcer swarm
Кластер postgresql c помощью stolon 
И приложения на django/python
***

### Ansible
Скрипты и настройки для разворачивания находятся(и инструкция как это выглядит)
[https://github.com/gytim/ifrri/ifrri-ansible/](https://github.com/gytim/ifrri/tree/master/ifrri-ansible/)

### DOCKER SWARM
Файлы для разворачивания, используемые выше находятся
[https://github.com/gytim/ifrri/ifrri-swarm/](https://github.com/gytim/ifrri/tree/master/ifrri-swarm/)


### source dockerfile
Недостающие docker образы
[https://github.com/gytim/ifrri/ifrri-docker-files/](https://github.com/gytim/ifrri/tree/master/ifrri-docker-files/)



## Принцип работы.

#### Подготовка
1. В самом начале нам необходимо собрать image(build в swarm не работает)
 В образе устанавливается psql для подключения к postgresql
 Сайт если не находит данных предлагает сделать migrate
2. Есть 4 места где указывается пароль:
 в образе newsite/newsite/settings.py, скрипте на создание чистой базы create_base.sh и 2 файла /etc/secrets/*

#### Разворачивание

1. Обновление системы
2. Установка необходимых пакетов в виртуалке
4. Клонирование github репы с sh и.yml файлами
5. Запуск 

#### Использование
[127.0.0.1:80](127.0.0.1:80)

По умолчанию web на 8000

Если не может подключиться к django таблице переводит к созданию базы

Если базы нет, то запускает создание (если база есть а данных нет, то все равно вызоветься скрипт, который ничего не сделает)

Дальше заполнение через миграцию базы.


*** 
