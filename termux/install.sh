#!/bin/bash

echo -e "\n\e[1;32m[!] In process of installation...\e[0m\n"

pkg install python -y

python -m pip install --upgrade pip

echo -e "\n\e[1;32m[!] The installation is complete and run the command: python sysindators.py\e[0m"
