# Big Data Federation Programming Challenge

This is my submission for the Big Data Federation programming challenge.

## Required:
1. Selenium for python3
2. venv for python3
3. Chrome web driver executable (v75.0.3770.80)

## Instructions
All commands are run from the main project directory.

1. To run the webscraper, enter the following:
``` bash
python3 python/scrape.py -d "/path/to/chromedriver"
```
2. To run the server, enter the following:
``` bash
source python/venv/bin/activate && python3 python/app.py
```
3. To make requests to the server, open up a new tab and enter GET requests like the following. Note there is no input validation:
``` bash
curl 'http://127.0.0.1:8080/commodity?start_date=2019-01-29&end_date=2019-06-06&commodity_type=gold'
```
