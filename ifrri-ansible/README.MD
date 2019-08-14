# ANSIBLE PLAYBOOK FOR RUNNING DOCKER-COMPOSE
  Разворачиваем проект с помощью ansible, в файлах(hosts, groups_vars/*) уже указан хост и данные для ssh 
  (сервер gytim.sknt.ru)

 ***
##Запуск деплоя на виртуалку
#### github.com/gytim/ifrri-ansible

Необходимо утстановленные:
* ansible
* git

Создаем папку
```
mkdir ifrri-ansible
```

Скачиваем с репы все добро для ansible
```
git clone https://github.com/gytim/ifrri/ifrri-ansible.git ifrri-ansible
cd ifrri-ansible
```
Запускаем bash( но можно перейти в папку ifrri-ansible/playbook и запускать их вручную :) )
 В зависимости от системы
   для `centos 7`
   
```
sh start_deploy_rpm.sh
```

 для `ubuntu 18.04`
   
```
sh start_deploy_deb.sh   
```

***
### SSH
Чтобы подключиться по ssh к виртуальной машине
    для `centos 7`

```
 ssh vagrant@gytim.sknt.ru:3022
```

    для `ubuntu 18.04`

```
ssh vagrant@gytim.sknt.ru:4022
```

### HTTP
Чтобы увидеть что на 80 порту виртуалок набрать
    для `centos 7`

```
gytim.sknt.ru/centos
```

    для `ubuntu 18.04`
    
```
gytim.sknt.ru/ubuntu
```

### Сброс виртуалки
Для разворачивания виртуалки заново в браузере набрать либо/либо
    для `centos 7`
    
[http://gytim.sknt.ru/vagrant/centos_reload/](http://gytim.sknt.ru/vagrant/centos_reload/)


    для `ubuntu 18.04`

[http://gytim.sknt.ru/vagrant/ubuntu_reload](http://gytim.sknt.ru/vagrant/ubuntu_reload)


и выполнить скрипт для перезапускаемой системы либо/либо
    для `centos 7`
    
```
sh zero_rpm.sh 
```

    для `ubuntu 18.04`
    
```
sh zero_deb.sh
```

* Установка виртуалок произведена из базового образа ubuntu 16.04 и dvd centos 7.

==============================================
для связи чтобы рассказать о моих ошибках, мне будет приятно
ahrimana@rambler.ru
 
