# [Web Scrapping](https://automatetheboringstuff.com/chapter11/)

## Web Browser Module `import webbrowser`

* This can launch a new browser to a specify URL with the `webbrowser.open()` method

* You can write simple scripts to automate getting some data from one website and inputting it into another.

## [Batch files](https://automatetheboringstuff.com/appendixb/)

* These are files that have command in them to run all other program automatically.

* Useful to automate something with just one word command and having all other scripts run


## Download files from website

* The `import requests` Module let you download files from web. It is a 3rd party module.

* `res = requests.get('URL')` will request for that page and return the page as a response object

* `res.status_code` You can check for status code with this

* `res.raise_for_status()` will return an error if there was a problem downloading the file

* If you want to write the file to a text file, you must write it as Write-Binary Mode `open(filename, 'wb')`


## Parsing HTML with BS4 module

* Beautiful Soup 4 help us parse HTML easily and it is a 3rd party module. ( See Sample Code )

## Control Browser with Selenium Module

* You must use `from selenium import webdriver` to use this module
