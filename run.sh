#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cd frontendapp && npm install 
cd ..
WEBID=`docker ps -aqf "name=cs5331_19_web"`
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker-compose build && docker-compose up
