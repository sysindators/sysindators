#!/bin/bash

echo -e "\n\e[1;32m[!] In process of installation...\e[0m\n"

pkg install python python2 python3 -y

pip install requests

pip install rich

pip install phonenumbers

pip install opencage

pip install folium

pip install geocoder

pip install bs4

pip install scapy

python -m pip install clear_cache

echo -e "\n\e[1;32m[!] The installation is complete and run the command: python sysindators.py\e[0m"