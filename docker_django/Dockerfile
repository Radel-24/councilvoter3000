FROM debian:buster

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install sqlite3 -y
RUN python3 -m pip install Django
RUN python3 -m pip install requests
RUN python3 -m pip install oauthlib
RUN python3 -m pip install requests-oauthlib
RUN python3 -m pip install django-oauth-toolkit
