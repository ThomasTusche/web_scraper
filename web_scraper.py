import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DRIVER_PATH = '/usr/bin/chromedriver'
URL = 'https://www2.hm.com/de_de/home/produkte/kissen.html'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("user-agent=[0]".format(user_agent))
options.add_argument("--window-size=1920,1200")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument('--remote-debugging-port=9222')

wd = webdriver.Chrome(options=options, executable_path=DRIVER_PATH, service_log_path='/usr/src/app/log.txt')

wd.delete_all_cookies()

wd.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like$


wd.get("https://www2.hm.com/de_de/home/produkte/kissen.html")

#result.click()

#time.sleep(4)

print(wd.page_source)
