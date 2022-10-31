#!/bin/bash

echo -e "\n\e[1;32m[!] In process of installation...\e[0m\n"

pkg install python python2 python3 -y

python -m pip2 install --upgrade homeassistant

pip2 install requests

pip2 install rich

pip2 install phonenumbers

pip2 install opencage

pip2 install folium

pip2 install geocoder

pip2 install bs4

pip2 install scapy

python -m pip2 install clear_cache

echo -e "\n\e[1;32m[!] The installation is complete and run the command: python sysindators.py\e[0m"
