FROM debian:buster

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y nginx
RUN apt-get install openssl -y
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx.key -out /etc/ssl/certs/nginx.crt -subj "/C=DE/ST=Baden Wuerrtemberg/L=Heilbronn/O=42Heilbronn/OU=Student/CN=council-vote.42heilbronn.de/emailAddress=radelwar@student.42heilbronn.de"
COPY ./default.conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]