#!/bin/bash
# Инициализация всех нод

cd /opt/i-free/test0/ifrri-swarm

docker init swarm

docker stack deploy --compose-file docker-compose_web.yml web
docker stack deploy --compose-file docker-compose-etcd.yml etcd
./bin/stolonctl init --cluster-name=stolon-cluster --store-backend=etcdv3 --store-endpoints=http://127.0.0.1:2379 -y
docker stack deploy --compose-file docker-compose-pg.yml pg
