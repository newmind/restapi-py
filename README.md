# 환경

실행 환경
* docker, docker-compose

개발 환경
* python 3.7
* mysql 5.7
* sqlAlchemy


## Build and Run
실행
```sh
docker-compose build
docker-compose run
```

테스트
```sh
# create
curl -X POST 'http://localhost:8080/tournament' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title":"test aaa",
	"gameName": "battle",
	"playerCount": 10,
	"location": "ONLINE"
}'

curl -X POST 'http://localhost:8080/tournament' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title":"test bb 2",
	"gameName": "lol",
	"playerCount": 10,
	"location": "ONLINE"
}'

# get 
curl -X GET http://localhost:8080/tournament/2

# delete 
curl -X GET http://localhost:8080/tournament/2
```

## Unit Test
```sh
 pip install -r app/requirements-dev.txt
 pytest app
```
