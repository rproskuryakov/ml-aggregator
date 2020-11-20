# Aggregator of articles on machine learning

## Description
This projects contains service that aggregates the last research articles on machine learning from the leading companies in AI, e.g. Google, Facebook and Yandex.

Frontend is written on [Angular](https://angular.io/), Backend on [FastAPI](). Articles gains with gelp of web-spiders on [Scrapy](https://scrapy.org/) which write them into [MongoDB](https://www.mongodb.com/).

## Launch application locally
To launch application you need to install (Docker)[https://docs.docker.com/engine/install/] and (docker-compose)[https://docs.docker.com/compose/install/], and than to start the service with the followind command:
```bash
docker-compose -f docker-compose.local.yml up
```
Frontend is located on localhost:4201.

## TO DO
* Add search on resource 
* Add search on tags (General ML, NLP, CV, RL и т. д.)
* Add authentification and button "add article to favourite"
* Add recommender system based on "favourites"
