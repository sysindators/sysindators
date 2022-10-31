#!/usr/bin/python

import os, sys, random, time

from clear_cache import clear as clear_cache
from os import system as bash
from sys import exit as logout
from bin import TrackLocation, XssScanner, SynFlood, SQLInjection
from requests import get as detectionIP
from rich.console import Console
from rich.table import Table


def starting(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)


def select():
    select_menu = input("sysindators > ")
    if select_menu == "show":
        table = Table()

        table.add_column("Command", no_wrap=False)
        table.add_column("Information", no_wrap=False)

        table.add_row("track_location", "Find someone's location by various methods")
        table.add_row(
            "xss_scanner",
            "Detects XSS vulnerability in web pages using requests and BeautifulSoup",
        )
        table.add_row(
            "syn_flood",
            "TCP SYN Flooding attack, which is a form of denial of service attack",
        )
        table.add_row(
            "sql_injection_detector",
            "Detect SQL Injection vulnerabilities in web applications using requests and BeautifulSoup",
        )

        console = Console()
        console.print(table)
        print("\n")
        select()
    elif select_menu == "track_location":
        print(" > Example: track_location/phone_number, track_location/ip\n")
        select()
    elif select_menu == "track_location/phone_number":
        print(
            "\n > Example: Enter a phone number that starts with your country code like +62 you take 62 for example +62851xxxxxxxx, then press enter to start the process\n"
        )
        NUMBER = input("sysindators > track_location > [phone_number] : ")
        TrackLocation.PhoneNumber(NUMBER)
    elif select_menu == "track_location/ip":
        print("\n > Example: Enter the Victim's IP Address to start the process\n")
        IP = input("sysindators > [ip] : ")
        TrackLocation.Ip(IP)
    elif select_menu == "xss_scanner":
        print("\n > Example: Enter the Victim's URL to start the process\n")
        URL = input("sysindators > [URL] : ")
        XssScanner.run(URL)
    elif select_menu == "syn_flood":
        print("\n > Example: Enter the Victim's IP Address to start the process\n")
        IP = input("sysindators > [IP] : ")
        SynFlood.run(IP)
    elif select_menu == "sql_injection_detector":
        print("\n > Example: Enter the Victim's URL to start the process\n")
        URL = input("sysindators > [URL] : ")
        SQLInjection.run(URL)
    elif select_menu == "clear":
        bash("clear")
        print("\n")
        select()
    elif select_menu == "exit":
        clear_cache(dir=".")
        logout(print(" > You Exit"))
    else:
        print(f" > {str(select_menu)}: Command not found\n")
        select()


def delete():
    bash("clear")


def main():
    starting(" > [!] Starting the Sysindators")
    re = detectionIP("https://api.myip.com").json()
    ip = re["ip"]
    list_tools = os.listdir("bin/__pycache__")
    table = Table(box=None)
    logo = f"""

░█▀▀░█░█░█▀▀░▀█▀░█▀█░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀▀
░▀▀█░░█░░▀▀█░░█░░█░█░█░█░█▀█░░█░░█░█░█▀▄░▀▀█
░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀                                                


=[ Sysindators v1.0.0 ]=
+ -- --=[ {str(len(list_tools))} Tools ]=-- -- +
+ -- --=[ You IP : {ip} ]=-- -- +
  """
    table.add_column(logo, style="cyan", no_wrap=False, justify="center")
    console = Console()
    delete()
    console.print(table)
    select()


main()
