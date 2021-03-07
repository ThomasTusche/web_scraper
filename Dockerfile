FROM python:3

WORKDIR /usr/src/app

RUN pip3 install boto3 && \
    pip3 install selenium

RUN sh -c 'echo "APT::Default-Release "stable";" >> /etc/apt/apt.conf' 
RUN sh -c 'echo "deb http://ftp.hr.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list'
RUN apt-get update -y && apt-get install -yt sid firefox

COPY . .

CMD [ "python3", "./web_scraper.py" ]