#!/bin/bash
# Скрипт по сборке stolonctl используемого для инициализации

cd /opt/i-free/test0/ifrri-swarm

mkdir stolon
git clone https://github.com/sorintlab/stolon.git stolon

cd stolon
chmod +x build
./build
chmod +x bin/stolonctl

mkdir /opt/i-free/test0/ifrri-swarm/ifrri-swarm/bin
cp bin/stolonctl /opt/i-free/test0/ifrri-swarm/ifrri-swarm/bin/stolonctl
cd ..
#rm -R stolon
