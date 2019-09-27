FROM zenika/alpine-chrome
LABEL Maintainer "Azeem Animashaun"
LABEL Purpose " Chrome Headless Selenium For Baseline Test "
LABEL For "Linuxjobber"
USER root
RUN apk add python3
USER chrome
RUN pip3 install yagmail selenium --user
RUN mkdir ~/qa 
#ENTRYPOINT ['/home/chrome/qa/start/sh']
