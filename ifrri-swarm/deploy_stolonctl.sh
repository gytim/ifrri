#!/bin/bash
# Скрипт по сборке stolonctl используемого для инициализации

mkdir stolon
git clone https://github.com/sorintlab/stolon.git stolon

cd stolon
chmod +x build
./build
chmod +x bin/stolonctl

cp -R bin /opt/i-free/test0/ifrri-swarm/ifrri-swarm
cd ..
#rm -R stolon
