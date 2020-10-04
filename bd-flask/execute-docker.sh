#docker network create --subnet 192.160.0.0/16 net-flask;
docker stop flask-bd-container
docker rm flask-bd-container
docker build -t flask-bd .
#docker run -d --net net-flask --ip 192.160.0.13 --env-file bd.env -p 3312:3306 --name flask-bd-container flask-bd
docker run -d --env-file bd.env -p 3312:3306 --name flask-bd-container flask-bd
docker start flask-bd-container
