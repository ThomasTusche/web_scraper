from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import boto3


DRIVER_PATH = './chromedriver'
URL = 'https://www2.hm.com/de_de/home/produkte/kissen.html'

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument('--remote-debugging-port=9222')

wd = webdriver.Chrome(options=options, executable_path=DRIVER_PATH, service_log_path='./log.txt')

wd.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})

wd.get(URL) # Gibt den HTML Code der Seite zurück.

sns = boto3.client('sns')

response = sns.publish(
    PhoneNumber='+4915162513577',
    Message='Artikel xyz ist jetzt bei H und M verfügbar!',    
)