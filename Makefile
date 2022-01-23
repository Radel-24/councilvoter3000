all:
	sudo docker-compose -f ./docker-compose.yml up
#	sudo docker-compose -f ./docker-compose.yml up -d

clean:
	sudo docker-compose -f ./docker-compose.yml down

fclean:
	sudo docker-compose -f ./docker-compose.yml down --volumes --rmi all

nginx:
	sudo docker-compose -f ./docker-compose.yml build nginx

web:
	sudo docker-compose -f ./docker-compose.yml build web

build:
	sudo docker-compose -f ./docker-compose.yml build