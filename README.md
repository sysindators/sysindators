# Sysindators Framework

[![Build status](https://github.com/termux/termux-app/workflows/Build/badge.svg)](https://github.com/sysindators/sysindators/actions)
[![Testing status](https://github.com/termux/termux-app/workflows/Unit%20tests/badge.svg)](https://github.com/sysindators/sysindators/actions)

Sysindators (System Intruders and Data Predators) is a tool framework made especially for hacking, has tools that help you to create extraordinary things.

Sysindators is the name of the team? Yes, that's the name of the team in the black hat category.

Documentation that can help you use Sysindators for hacking: -

**Official Website:** -

> **Disclaimer:** Please do not use this on a device you don't own or do not have permission to. We do not take any responsibility.

<a href="./TOOLS.md">**List Tools**</a>

## How to use
To run Sysindators we can type command ``show`` it will bring up all tools list framed by table.

> **Note**: Sysindators recommend using python version 3.10 or 3.10.8, Sysindators is not yet stable in python 3.11

![Sysindators](https://user-images.githubusercontent.com/115671161/199221182-1cbd11cc-d980-4ce7-9164-c4bad1e550d1.jpg)

## Installation

### Installation for Linux
```bash
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/sysindators/sysindators
cd sysindators
pip3 install -r requirements.txt
python3 sysindators.py
```
### Installation for Termux
```bash
pkg update
pkg upgrade
pkg install git python
git clone https://github.com/sysindators/sysindators
cd sysindators
pip3 install -r requirements.txt
python3 sysindators.py
```

### Installation for Windows
First install Python and Git Bash on the official website below:
- [**Python**](https://www.python.org)
- [**Git Bash**](https://git-scm.com/downloads)

If everything is installed, please open one of the CMD, Windows PowerShell, or Git Bash and enter the command below:
```bash
git clone https://github.com/sysindators/sysindators
cd sysindators
pip3 install -r requirements.txt
python3 sysindators.py
```


## Fix Bugs
If you get a notification like this when you run Sysindators, follow our steps to fix this problem:
```bash
Traceback (most recent call last):
  File "C:\Users\Brand\OneDrive\Desktop\sysindators\sysindators.py", line 88, in <module>
    main()
  File "C:\Users\Brand\OneDrive\Desktop\sysindators\sysindators.py", line 84, in main
    console.print(table)
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\console.py", line 1667, in print
    with self:
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\console.py", line 869, in __exit__
    self._exit_buffer()
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\console.py", line 827, in _exit_buffer
    self._check_buffer()
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\console.py", line 2024, in _check_buffer
    legacy_windows_render(buffer, LegacyWindowsTerm(self.file))
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\_windows_renderer.py", line 17, in legacy_windows_render
    term.write_styled(text, style)
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\_win32_console.py", line 442, in write_styled
    self.write_text(text)
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\site-packages\rich\_win32_console.py", line 403, in write_text
    self.write(text)
  File "C:\Users\Brand\AppData\Local\Programs\Python\Python310\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode characters in position 16-59: character maps to <undefined>
```
Run the command below, and restart Sysndators:
```bash
chcp.com 65001
export PYTHONIOENCODING=utf-8
python3 sysindators.py
```

# Contributors

<a href="https://github.com/sysindators/sysindators/graphs/contributors">
  <img width="20%" src="https://contrib.rocks/image?repo=sysindators/sysindators" />
</a>
