# Bitly console utility

Small conslole utility for create short link via bitly services and count following a bitly links.
Use full link for your web resource as console argument to create short 'bytlink' or use 'bytlink' to cout following.
```
python main.py https://example.com
>>>
Вы ввели ссылку на сайт для сокращения ее на bitly
Вот ее битлинк: https://bit.ly/3NmOOK5

python main.py https://bit.ly/3NmOOK5
>>>
Вы ввели уже существующую ссылку с bitly.
По этой ссылке перешли 0 раз.
```
### How to install

1. For make it work you want to create bitly api token. You can generate it in bitly website - https://app.bitly.com/settings/api/
2. Create .env file in utility work directory
3. Enter in .env file one line:
```
BITLY_TOKEN='YOUR BITLY TOKEN'
```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).