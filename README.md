# Sysindators V1.0.0

Sysindators (System Intruders and Data Predators) is a tool framework made especially for hacking, has tools that help you to create extraordinary things.

Sysindators is the name of the team? Yes, that's the name of the team in the black hat category.

Documentation that can help you use Sysindators for hacking: -

**Official Website:** -

**Disclaimer:** Please do not use this on a device you don't own or do not have permission to. We do not take any responsibility.

## How to use
To run Sysindators we can type command ``show`` it will bring up all tools list framed by table.
![Sysindators](https://user-images.githubusercontent.com/115671161/199219702-3b2a436b-1e98-4ed7-9803-d7f8bb6f1773.png)

## Installation

### Installation for Linux
```shell
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/sysindators/sysindators
cd sysindators
pip install -r requirements.txt
python sysindators.py
```
### Installation for Termux
```shell
pkg update
pkg upgrade
pkg install git python
git clone https://github.com/sysindators/sysindators
cd sysindators
pip install -r requirements.txt
python sysindators.py
```

### Installation for Windows
First install Python and Git Bash on the official website below:
- [**Python**](https://www.python.org)
- [**Git Bash**](https://git-scm.com/downloads)

If everything is installed, please open one of the CMD, Windows PowerShell, or Git Bash and enter the command below:
```shell
git clone https://github.com/sysindators/sysindators
cd sysindators
pip install -r requirements.txt
python sysindators.py
```


## Fix Bugs
If you get a notification like this when you run Sysindators, follow our steps to fix this problem:
```shell
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
```shell
chcp.com 65001
export PYTHONIOENCODING=utf-8
python sysindators.py
```

# Contributors

<a href="https://github.com/sysindators/sysindators/graphs/contributors">
  <img width="20%" src="https://contrib.rocks/image?repo=sysindators/sysindators" />
</a>
