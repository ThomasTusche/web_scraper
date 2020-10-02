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
- Chrome Beta

## Important

Selenium was using my chrome browser but currently only Version 85 is stable. Selenium had problems with this and needed Version 86.
To work around it I used a Docker Container with Python 3 image.

There you can easily download the Chrome beta version without causing trouble to your current browser:

### install chrome beta
wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-beta/google-chrome-beta_86.0.4240.68-1_amd64.deb
dpkg -i google-chrome-beta_86.0.4240.68-1_amd64.deb
apt-get -f install 

## Drivers
In case you need the right driver, you can download them for all browsers here: https://pypi.org/project/selenium/
Just save them somewhere and adjust the path in your python script.
The chrome driver for example is already is this project.