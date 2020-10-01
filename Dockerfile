FROM python:3

WORKDIR /usr/src/app

COPY . ./

RUN apt update

RUN pip3 install selenium

CMD tail -f /dev/null

# install chrome beta
    # wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-beta/google-chrome-beta_86.0.4240.68-1_amd64.deb
    # dpkg -i google-chrome-beta_86.0.4240.68-1_amd64.deb
    # apt-get -f install 
