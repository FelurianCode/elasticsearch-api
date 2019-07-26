# elasticsearch-api

## Requirements:
* Python3
* Django2.0.3
* djangorestframework
* pymongo
* mongodb
* elasticsearch

### Installing requirements
```
python3 -m venv env && source env/bin/activate
pip3 install Django==2.0.3
pip3 install djangorestframework
pip3 install pymongo
brew update
brew install mongodb
pip3 install elasticsearch-dsl
```

### Setting elasticsearch locally
```
mkdir elasticsearch
cd elasticsearch
Download from https://www.elastic.co/es/downloads/elasticsearch
(extract the contents)
Run elastic search:
./elasticsearch-7.2.0/bin/elasticsearch

```

### Dbs
Change db name in api_app/search.py


### Run project 
```
python3 manage.py runserver
```


### Project endpoints
```
GET   http:/{YOUR_URL}/api/elastic/       -->   Bulks mongo data to elasticsearch
GET   http:/{YOUR_URL}/api/tweets-date/   -->   Gets tweets ordered by date
GET   http:/{YOUR_URL}/api/tweets-user/?user={preferredUsername}   -->   Gets tweets by users   
```

