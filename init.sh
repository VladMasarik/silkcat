#!/bin/bash
mkdir folder
cd folder
git clone https://github.com/VladMasarik/silkcat.git
cd silkcat
IP=`hostname -I | awk '{print $1}'`
sudo python3 manage.py runserver $IP:80
