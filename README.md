# web_scraper
Python Programm to scrape websites and get notifications via Amazaon SNS

## Disclaimer
The script is used to scrape websites and receive SMS notifications by using the AWS Service SNS. To run it automatically I created a Dockerfile which you can build into an image and run it every x minutes by leveraging the AWS Cloudwatch Service in combination with AWS ECS.
To find a full explanation in german please visit my website -> https://codemonkey.tech/python-webscraper-mit-sms/

## Tools Used

- Python 3
- Selenium

## Drivers
In case you need the right driver, you can download them for all browsers here: https://pypi.org/project/selenium/
Just save them somewhere and adjust the path in your python script.
The chrome driver for example is already in this project.
