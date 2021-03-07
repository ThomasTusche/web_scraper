from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import boto3

options = Options()
options.headless = True
options.log.level = "trace"

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

browser = webdriver.Firefox(options=options, executable_path='./geckodriver', service_log_path='./log_test.txt')

browser.get('https://www.lidl.de/de/parkside-performance-akku-drehschlagschrauber-1-2-passp-20-li-a1-ohne-akku-und-ladegeraet/p361369')

html = browser.find_element_by_id("add-to-cart")

test = html.get_attribute("disabled")


time.sleep(2)

if test == "true":

    print("No Email Send")

else:
    
    sns = boto3.client('sns')

    response = sns.publish(
        PhoneNumber='+491778556587',
        Message='Akku-Drehschlagschrauber wieder verfügbar -> https://www.lidl.de/de/parkside-performance-akku-drehschlagschrauber-1-2-passp-20-li-a1-ohne-akku-und-ladegeraet/p361369',    
    )

    print("Email Send")

