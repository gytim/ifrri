# Docker Swarm
### cluster postgresql on stolon and django web
***
Простой кластер базы с использованием [stolon](https://github.com/sorintlab/stolon) и веб приложения как фронт.

Разворачивается с помощью правил:
docker-compose_web.yml
docker-compose-etcd.yml
docker-compose-pg.yml

#### docker-compose_web.yml
2шт реплик, управление отдаем swarm
*Можно поставить еще и перезапуска но не будем мешать тестированию.

#### docker-compose-etcd.yml + docker-compose-pg.yml
Развернут по стандарту.

#### stolonctl
Необходимо для разворачивания, собирается stolon с помощью скрипта deploy_stolonctl.sh 
***
etc/secrets/*

pgsql, pgsql_repl устанавливаються пароли для пользователя postgres
(pgsql еще должен совпадать с паролем в докере)
