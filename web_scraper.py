from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = './chromedriver'
URL = 'https://www2.hm.com/de_de/home/produkte/kissen.html'


### some of those options were recommend in case you receive errors. For me it worked without them but if you face problems,
### it might help to remove the comments below.

options = Options()
options.add_argument("--no-sandbox")
#options.add_argument("user-agent=[0]".format(user_agent))
#options.add_argument("--window-size=1920,1200")
#options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument('--remote-debugging-port=9222')

wd = webdriver.Chrome(options=options, executable_path=DRIVER_PATH, service_log_path='./log.txt')

#wd.delete_all_cookies()
wd.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})

wd.get(URL)

print(wd.page_source)