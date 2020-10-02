# web_scraper
Python Programm to scrape the H&amp;M Website for specific products

## Disclaimer
The german version of H&amp;M Home Website (https://www2.hm.com/de_de/home/produkte/) blocks scripts from scraping their website.
If you use 'Selenium' with the *headless* option, you get an **access denied** notification.
To solve this, you have to change the *user_agent* part for your request like I did in my code.

Now you should be able to scrape the website and extract any data you want.

## Tools Used

- Python 3
- Selenium

## Drivers
In case you need the right driver, you can download them for all browsers here: https://pypi.org/project/selenium/
Just save them somewhere and adjust the path in your python script.
The chrome driver for example is already in this project.