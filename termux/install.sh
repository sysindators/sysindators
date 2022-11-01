#!/bin/bash

echo -e "\n\e[1;32m[!] In process of installation...\e[0m\n"

pkg install python python2 python3 -y

python -m pip install --upgrade homeassistant

echo -e "\n\e[1;32m[!] The installation is complete and run the command: python sysindators.py\e[0m"
