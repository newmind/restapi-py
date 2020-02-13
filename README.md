# 환경

실행 환경
* docker (> 19.0), docker-compose (> 1.25)

개발 환경
* python 3.7
* mysql 5.7
* sqlAlchemy


## Build and Run on Docker

두개의 컨테이너로 구성 
* app : flask app
* db : mysql db
 
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

# patch
curl -X PATCH 'http://localhost:8080/tournament/2' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title":"2 modified",
	"gameName": "bonjour",
	"playerCount": 30,
	"location": "ONLINE"
}'

# search
curl -X GET 'http://localhost:8080/search?keyword=test'

# delete 
curl -X DELETE http://localhost:8080/tournament/2


```

## Unit Test
```sh
 pip install -r app/requirements-dev.txt
 pytest app
```


## db schema

mysql docker 최초 실행시에  [init.sql](db\init.sql) 스크립트 실행됨
