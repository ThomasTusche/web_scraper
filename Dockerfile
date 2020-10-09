FROM python:3

WORKDIR /usr/src/app

RUN pip3 install boto3 && \
    pip3 install selenium

RUN apt update && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install ./google-chrome-stable_current_amd64.deb -y

COPY . .

CMD [ "python3", "./web_scraper.py" ]